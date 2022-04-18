import imp
from venv import create
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    ListView,
)

from account.models import *
from account.forms import *
from data.models import *

from django.contrib.auth import login as auth_login
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

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
        create_form = createUserForm()

        context = {
            "form": form,
            "create_form": create_form
        }
    return render(request, "login.html", context)

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
    user = Account.objects.filter(is_superuser=False).count()
    rest = Restaurant.objects.all().count()
    context = {
        "user_count" : user,
        "rest_count" : rest
    }
    return render(request, "home.html", context)

class ViewUserView(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'accounts.view_account'
    raise_exception = True

    def post(self, request, pk, *args, **kwargs):
        user = Account.objects.get(account_id=pk)
        form = viewUserForm(request.POST, instance=user)
        return redirect("userlist")

    def get(self, request, pk, *args, **kwargs):
        user = Account.objects.get(account_id=pk)
        form = viewUserForm(instance=user)
        context = {
            "form": form,
            "pk": pk
        }
        return render(request, "profile.html", context)

class EditUserView(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'accounts.change_account'
    raise_exception = True

    def post(self, request, pk, *args, **kwargs):
        user = Account.objects.get(account_id=pk)
        form = editUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            role = request.POST.get("role")
            user.save()

            messages.success(request, "Successfully updated profile!")
            return redirect(f'/viewUser/{user.account_id}')
        else:
            form = editUserForm(instance=user)
            extra_context = {
                "form": form,
            }
            print('something wrong')
            messages.error(request, "Invalid input! Please input a valid information.")
            return render(request, "editUser.html", extra_context)

    def get(self, request, pk, *args, **kwargs):
        user = Account.objects.get(account_id=pk)
        form = editUserForm(instance=user)
        extra_context = {
            "form": form,
        }
        return render(request, "editUser.html", extra_context)

class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'accounts.view_account'
    template_name = "userList.html"
    queryset = Account.objects.all()

class UpdateProfilePicView(View, LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'accounts.change_account'
    raise_exception = True

    def post(self, request, pk, *args, **kwargs):
        user = Account.objects.get(account_id=pk)
        user.profile_pic = request.FILES.get('profile-pic')
        user.save()
        return redirect('viewUser', pk)

def deleteUser(request, event_id):
    event = Account.objects.get(pk=event_id)
    event.delete()
    return redirect('userlist')