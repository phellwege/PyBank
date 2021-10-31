from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request, 'home.html')

def regis(request):
    errors = User.objects.emailValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register_page')
    else:
        pw_hash = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash
        )
        request.session['uuid'] = user.id
    return redirect('/character_selector')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/login_page')
    else:
        user = User.objects.filter(email=request.POST['email'])
        request.session['uuid'] = user[0].id
        return redirect('/character_selector')

def logout(request):
    request.session.clear()
    return redirect('/')

def login_page(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def signout(request):
    if 'Character_ID' in request.session:
        del request.session['Character_ID']
    return redirect('/character_selector')

