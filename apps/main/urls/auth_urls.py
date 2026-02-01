from django.urls import path
from django.contrib.auth import views as django_auth_views
from apps.main.views import auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", auth_views.register, name="register"),

    path(
    "password-reset/",
    auth_views.DebugPasswordResetView.as_view(template_name="auth/password_reset.html"),
    name="password_reset",
),

    path("password-reset/done/",
         django_auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/",
         django_auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path("reset/done/",
         django_auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"),
         name="password_reset_complete"),
]
