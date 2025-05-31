# Users Views file

from functools import lru_cache
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, login_not_required


@login_not_required
@lru_cache(maxsize=None)
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect("login")

            except IntegrityError:
                messages.error(request, 'Username or email already exists')
                return render(request, 'users/signup.html')

        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'users/signup.html')

    return render(request, "users/signup.html")


@login_not_required
@lru_cache(maxsize=None)
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")

        else:
            messages.error(request, 'Invalid username or password')
            return render(request, "users/login.html")

    return render(request, "users/login.html")


@login_required(login_url="login")
def log_out(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")