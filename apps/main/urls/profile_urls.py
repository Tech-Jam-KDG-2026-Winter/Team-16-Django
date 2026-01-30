from django.urls import path
from . import profile_views

app_name = "profile"

urlpatterns = [
    path("<str:username>/", profile_views.profile_detail, name="detail"),
    path("edit/", profile_views.profile_edit, name="edit"),
    path("delete/", profile_views.profile_delete, name="delete"),
]