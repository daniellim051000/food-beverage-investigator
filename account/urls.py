import imp
from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("home", views.homepage, name="home"),
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name="register"),
]