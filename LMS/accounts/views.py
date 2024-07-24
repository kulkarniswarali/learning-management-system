from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .decorators import *

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # username = request.POST.get('username')
        # print(email, password)
        
        user = authenticate(request, email = email , password = password)
        print('authenticated')
        print(user)
        
        if user is not None:
           login(request,user)
           return redirect('index')
        else:
            messages.info(request, 'Email or Password is Incorrect')
            return redirect('login')

    return render(request , 'accounts/login.html')


@unauthenticated_user
def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get('first_name')
            user = form.save()
            messages.success(request, 'Account created for {}! You are now able to log in'.format(fname))
            return redirect('login')

    return render(request, 'accounts/register.html', {'form': form})