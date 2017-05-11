# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from login.forms import *

 
def register(request, template_name='login/register.html'):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            return redirect('register_success')
    else:
        form = RegistrationForm()

    return render(request, template_name, { 'form': form } )
 

def register_success(request, template_name='login/success.html'):
    return render(request, template_name)

def home(request, username, password, template_name='login/home.html'):
    
    login - get_object_or_404(RegistrationForm, username=username, password=password)
    form = RegistrationForm(request.POST or None, instance = login)

    if request.method == 'POST':
         return redirect('home')

    return render(request, template_name, {'user': request.user})   
 

def logout_page(request):
    logout(request)
    return redirect('login')
 

def login(request, template_name='login/login.html'):
    form = RegistrationForm()    
    return render(request, template_name, { 'form' : form } )