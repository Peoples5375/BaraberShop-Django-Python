from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('about', views.about),
    path('dashboard', views.dashboard),
    path('new_barber', views.new_barber),
    path('details/<id>', views.details),
    path('post_review/<id>', views.review),
    path('edit_barber', views.edit_barber),
    path('make_admin', views.make_admin),
    path('logout', views.logout)
]   