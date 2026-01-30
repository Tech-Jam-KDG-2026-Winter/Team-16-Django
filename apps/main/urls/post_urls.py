from django.urls import path
from ..views import post_views

urlpatterns = [
    path("", post_views.post_list, name="post_list"),
    path("create/", post_views.post_create, name="post_create"),
    path("<int:post_id>/", post_views.post_detail, name="post_detail"),
    path("<int:post_id>/edit/", post_views.post_edit, name="post_edit"),
    path("<int:post_id>/delete/", post_views.post_delete, name="post_delete"),
]