# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm, ProfileForm
from .models import UserProfile

def signin(request):
    form = LoginForm()
    if request.method == 'GET':
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile')
            else:
                error = 'Пользователь неактивен'
                return render(request, 'login.html', {'error': error, 'form': form})
        else:
            error = 'Неверная пара логин-пароль'
            return render(request, 'login.html', {'error': error, 'form': form})

def signup(request):
    form = SignupForm()
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': form})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']
        if password != password_confirmation:
            error = 'Пароль и подтверждение не совпадают'
            return render(request, 'signup.html', {'form': form, 'error': error})
        user, created = User.objects.get_or_create(username=username, email=email)
        if created:
            user.set_password(password)
            user.save()
            UserProfile.objects.create(name=username,user=user)
            return redirect('profile')
        else:
            error = 'Пользователь с таким логином или адресом электронной почты уже существует'
            return render(request, 'signup.html', {'form': form, 'error': error})

def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def profile(request):
    userprofile = UserProfile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        userprofile.name = request.POST['name']
        userprofile.save()
    form = ProfileForm(initial={'name': userprofile.name})
    return render(request, 'profile.html', {'username': request.user.username, 'form': form})
