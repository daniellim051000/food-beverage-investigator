from venv import create
from django.shortcuts import render, redirect

from account.models import *
from account.forms import *

from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        form = loginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            print("succesful login")

            remember_me = form.cleaned_data["remember_me"]
            if remember_me:
                request.session.set_expiry(1209600)
            return redirect("home")
        else:
            messages.warning(request, 'There is an issue with your login processes')
            return redirect("login")
    else:
        form = loginForm()

    return render(request, "login.html", {"form": form})

def logout(request):
    auth.logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        create_form = createUserForm(data=request.POST)
        if create_form.is_valid():
            user = create_form.save(commit=False)
            user.save()
            messages.success(request, "User created successfully!")
            return redirect("login")
        else:
            messages.error(request, "User creation failed")
    else:
        create_form = createUserForm()
    return render(request, "login.html", {"create_form": create_form})

def homepage(request):
    return render(request, "home.html")