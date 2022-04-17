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
    path("userlist", views.UserListView.as_view(), name="userlist"),
    path("viewUser/<uuid:pk>/", views.ViewUserView.as_view(), name="viewUser"),
    path("editUser/<uuid:pk>/", views.EditUserView.as_view(), name="editUser"),
    path("deleteUser/<event_id>/", views.deleteUser, name="deleteUser"),
    path("updateProfilePic/<uuid:pk>/", views.UpdateProfilePicView.as_view(), name="updateProfilePic"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)