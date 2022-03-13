from django.shortcuts import render, redirect

from account.models import *
from account.forms import *

from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        form = loginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            if user.role != "Operator" and user.role != "Supervisor":
                auth_login(request, user)
                print("succesful login")

                remember_me = form.cleaned_data["remember_me"]
                if remember_me:
                # print(remember_me)
                    request.session.set_expiry(1209600)

            # print(request.user.is_authenticated) # testing
                return redirect("home")
            else:
                messages.warning(request, 'There is an issue with your login processes')
                return redirect("login")
        else:
            print("not succesful login")
    else:
        form = loginForm()
    return render(request, "login.html", {"form": form})