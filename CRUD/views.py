# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404

from django.forms import ModelForm
from CRUD.models import Crud, Log
from .forms import CrudForm, LoginForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="login/")
def home(request, template_name= "CRUD/bootstrap-admin.html"):
    form = LoginForm(request.POST or None) 
    return render(request, template_name, { 'form' : form})



def index(request, template_name='CRUD/index.html'):

    if request.user.is_authenticated():
        CRUD = Crud.objects.all()
        data = {}
        data['object_list'] = CRUD
    else :
        return redirect ('home')

    return render(request, template_name, data)


def std_list(request, template_name = 'CRUD/std_list.html'):
    if request.user.is_authenticated():
        CRUD = Crud.objects.all()
        data = {}
        data['object_list'] = CRUD
    else :
        return redirect('home')

    return render(request, template_name, data)


def std_create(request, template_name = 'CRUD/std_create.html'):
    form = CrudForm(request.POST or None)
    
    if request.user.is_authenticated():
    
        if form.is_valid():
            form.save()
            return redirect('std_list')

    else :
        return redirect('home')
        
    return render(request, template_name, {'form' : form })
    

def std_update(request, pk, template_name='CRUD/std_create.html'):
    if request.user.is_authenticated():
        CRUD = get_object_or_404(Crud, pk=pk)
        form = CrudForm(request.POST or None, instance = CRUD)
        if form.is_valid():
            form.save()
            return redirect('std_list')
    
    else :
        return redirect('home')

    return render(request, template_name, {'form': form})
    
    
def std_delete(request,pk, template_name='CRUD/std_con_del.html'):
    if request.user.is_authenticated():
        CRUD = get_object_or_404(Crud, pk=pk)
        if request.method == 'POST':
            CRUD.delete()
            return redirect('std_list')
    else :
        return redirect('home')

    return render(request, template_name, {'object': CRUD})
    
