from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from .models import Profile
from .models import Review
import bcrypt

def index (request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.login_validator(request.POST)
    print(request.POST)
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    print(pw_hash)
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    else:   
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash, usertype = 'user')

        request.session['userid'] = user.id
        return redirect('/about')
    
            
    return redirect('/')

def login(request):
        user = User.objects.filter(email = request.POST['email'])
        print(user)
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                if logged_user.usertype == "admin":
                    return redirect('/dashboard')
                else:
                    return redirect('/about')

            else:
                messages.error(request, "Email/password is incorrect.")
        else:
            messages.error(request, "Email isnt registered yet.")
        return redirect('/')

def about(request):
    barbers = Profile.objects.all()
    context ={
        'barbers' : barbers
    }
    return render(request,'about.html', context)

def dashboard(request):
    barbers = Profile.objects.all()
    context ={
        'temp_admin' : User.objects.get(id= request.session['userid']),
        'barbers' : barbers,
        'users' : User.objects.all()
    }
    return render(request,'dashboard.html', context)

def edit_barber(request):
    c = Profile.objects.get(id=request.POST['barber_select'])
    c.phone_number = request.POST['phone_number']
    c.schedule = request.POST['schedule']
    c.experiance = request.POST['experiance']
    c.fun_facts = request.POST['fun_facts']
    c.save()
    return redirect('/dashboard')

def make_admin(request):
    c = User.objects.get(id=request.POST['user_select'])
    c.usertype = 'admin'
    c.save()
    return redirect('/dashboard') 

def new_barber(request):
    Profile.objects.create(
    first_name = request.POST['first_name'],
    last_name = request.POST['last_name'],
    phone_number = request.POST['phone_number'],
    schedule = request.POST['schedule'],
    experiance = request.POST['experiance'],
    fun_facts = request.POST['fun_facts']

    )
    return redirect('/dashboard')

def details(request, id):
    single_barber = Profile.objects.get(id=id)
    context = {
        'single_barber' : single_barber,
        # 'thereviews' : Review.objects.get(id=id)
    }

    return render(request, 'details.html', context)

def review(request, id):
    single_barber = Profile.objects.get(id=id)
    single_user = User.objects.get(id = request.session['userid'])

    Review.objects.create(review_post=request.POST["review_post"], rating = request.POST['select_rating'],
    barber_review = single_barber,
    created_by = single_user)
    return redirect(f'/details/{single_barber.id}')




def logout (request):
    request.session.clear()
    return redirect('/')
