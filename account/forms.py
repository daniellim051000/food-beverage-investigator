from django import forms
from django.contrib.auth.forms import AuthenticationForm

class loginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        label=("Remember Me"), initial=False, required=False
    )
