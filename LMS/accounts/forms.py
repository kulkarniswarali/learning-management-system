from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

    
class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control form-control-xl', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control form-control-xl', 'placeholder': 'Confirm Password'}))


    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
    
        labels ={
            'email': 'Email'
        }
        widgets = {
            'email' : forms.EmailInput(attrs={'class':'form-control form-control-xl', 'placeholder':'Email'}),
            'first_name' : forms.TextInput(attrs = {'class':'form-control form-control-xl', 'placeholder': 'First Name'}),
            'last_name' : forms.TextInput(attrs = {'class':'form-control form-control-xl', 'placeholder': 'Last Name'}),
        }