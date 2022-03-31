from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.dashboard_view, name="dashboard_view"),
]