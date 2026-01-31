from django.urls import path
from apps.main.views import admin_views

app_name = "admin_pages"

urlpatterns = [
    path("dashboard", admin_views.dashboard, name="dashboard"),
    path("users/", admin_views.user_list, name="user_list"),
    path("users/<int:user_id>/", admin_views.user_detail, name="user_detail"),
    path("users/<int:user_id>/toggle/", admin_views.user_toggle_active, name="user_toggle"),
    path("posts/", admin_views.post_list, name="post_list"),
    path("posts/<int:post_id>/delete/", admin_views.post_delete_confirm, name="post_delete_confirm"),
]