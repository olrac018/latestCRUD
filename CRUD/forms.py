from django import forms
from .models import Crud, Log
from django.contrib.auth.forms import AuthenticationForm 


class CrudForm(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ['stdno', 'fname', 'lname']

class LoginForm(AuthenticationForm):
    class Meta:
    	model = Log
    	fields = ['un', 'pw']

    		