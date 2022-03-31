from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.list_restaurant, name="data_list"),
    path("add_data", views.add_restaurant, name="add_data"),
]