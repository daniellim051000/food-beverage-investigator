from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.list_restaurant, name="data_list"),
    path("add_data", views.add_restaurant, name="add_data"),
    path("add_review", views.add_review, name="add_review"),
    path("edit_restaurant", views.edit_restaurant, name="edit_restaurant"),
    path("list_review", views.list_review, name="list_review"),
    
]