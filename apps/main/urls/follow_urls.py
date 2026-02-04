from django.urls import path
from apps.main.views import follow_views

app_name = "follow"

urlpatterns = [
    path("<str:username>/followers/", follow_views.followers_list, name="followers"),
    path("<str:username>/following/", follow_views.following_list, name="following"),
    path("<str:username>/toggle/", follow_views.follow_toggle, name="toggle"),
]