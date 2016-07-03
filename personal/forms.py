# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100)

class SignupForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100)
    email = forms.CharField(label='Электронная почта', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='Подтверждение', max_length=100, widget=forms.PasswordInput())

class ProfileForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
