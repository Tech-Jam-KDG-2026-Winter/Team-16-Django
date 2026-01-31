from django.urls import path
from apps.main.views import dashboard_views

app_name = "dashboard"

urlpatterns = [
    path("", dashboard_views.dashboard, name="dashboard"),
    path("users/", dashboard_views.user_list, name="user_list"),
    path("users/<int:user_id>/", dashboard_views.user_detail, name="user_detail"),
    path("users/<int:user_id>/toggle/", dashboard_views.user_toggle_active, name="user_toggle"),
    path("posts/", dashboard_views.post_list, name="post_list"),
    path("posts/<int:post_id>/delete/", dashboard_views.post_delete_confirm, name="post_delete_confirm"),
]