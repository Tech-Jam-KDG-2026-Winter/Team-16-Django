from django.urls import path
from apps.main.views import reaction_views

app_name = "reaction"

urlpatterns = [
    path("<int:post_id>/like/", reaction_views.like_post, name="like"),
    path("<int:post_id>/unlike/", reaction_views.unlike_post, name="unlike"),
]
