# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404

from django.forms import ModelForm

from CRUD.models import Crud
from .forms import CrudForm


def index(request, template_name='CRUD/index.html'):
    CRUD = Crud.objects.all()
    data = {}
    data['object_list'] = CRUD
    return render(request, template_name, data)

def login(request, template_name='CRUD/login.html'):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
    else:
        return HttpResponseRedirect('login')

    return render(request, template_name)



def std_list(request, template_name = 'CRUD/std_list.html'):
    CRUD = Crud.objects.all()
    data = {}
    data['object_list'] = CRUD
    return render(request, template_name, data)


def std_create(request, template_name = 'CRUD/std_create.html'):
    form = CrudForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('std_list')
    return render(request, template_name, {'form' : form })
    

def std_update(request, pk, template_name='CRUD/std_create.html'):
    CRUD = get_object_or_404(Crud, pk=pk)
    form = CrudForm(request.POST or None, instance = CRUD)
    if form.is_valid():
        form.save()
        return redirect('std_list')
    return render(request, template_name, {'form': form})
    
    
def std_delete(request,pk, template_name='CRUD/std_con_del.html'):
    CRUD = get_object_or_404(Crud, pk=pk)
    if request.method == 'POST':
        CRUD.delete()
        return redirect('std_list')
    return render(request, template_name, {'object': CRUD})
    
    