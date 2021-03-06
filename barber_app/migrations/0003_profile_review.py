# Generated by Django 2.2 on 2020-02-26 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barber_app', '0002_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('phone_number', models.CharField(max_length=45)),
                ('schedule', models.CharField(max_length=45)),
                ('experiance', models.CharField(max_length=255)),
                ('fun_facts', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_post', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('barber_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_barber_review', to='barber_app.Profile')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_review', to='barber_app.User')),
            ],
        ),
    ]
