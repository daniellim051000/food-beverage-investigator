from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, UsernameField

from account.models import Account

class loginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        label=("Remember Me"), initial=False, required=False
    )
    username = UsernameField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'type': 'text', 'name': 'txt'}
    ))
    password = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Password', 'type': 'password', 'name': 'pswd'}
    ))


class createUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Full Name."}), 
        label="Full Name",
    )
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email."}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Please enter contact number."}),
        label="Contact Number",
    )
    class meta:
        model = Account
        fields = ("username","name","email","contact_number")