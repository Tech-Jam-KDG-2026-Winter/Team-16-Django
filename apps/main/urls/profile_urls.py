from django.urls import path
from apps.main.views import profile_views

app_name = "profile"

urlpatterns = [
    path("edit/", profile_views.profile_edit, name="edit"),          # ★先に書く
    path("delete/", profile_views.profile_delete, name="delete"),
    path("<str:username>/", profile_views.profile_detail, name="detail"),
]