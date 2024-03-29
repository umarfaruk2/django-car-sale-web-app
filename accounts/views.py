from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth

def register(request):
    if request.method == 'POST':
        fm = RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('login')
    else:
        fm = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': fm})


def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data = request.POST)
        if fm.is_valid():
            user_username = request.POST.get('username')
            user_pass = request.POST.get('password')
            user = authenticate(username = user_username, password = user_pass)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        fm = AuthenticationForm() 
    return render(request, 'accounts/login.html', {'form': fm})


def user_logout(request):
    logout(request)
    
    return redirect('login')