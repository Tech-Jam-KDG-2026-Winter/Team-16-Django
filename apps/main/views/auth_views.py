from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse_lazy

from django import forms
from django.contrib.auth.models import User

from django.contrib.auth import views as django_auth_views
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


# Django 標準の認証ビューを利用
class LoginView(auth_views.LoginView):
    template_name = "auth/login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("post_list")  # or profile:detail
        return super().dispatch(request, *args, **kwargs)

LogoutView = auth_views.LogoutView.as_view(
    next_page=reverse_lazy("top")
)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="メールアドレス")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 登録後に自動ログイン
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegisterForm()

    return render(request, "auth/register.html", {"form": form})




class DebugPasswordResetView(django_auth_views.PasswordResetView):
    """
    開発用：送信するリセットURLをターミナルに出す
    """
    def form_valid(self, form):
        # フォームから対象ユーザーを取得（存在する分だけ）
        users = list(form.get_users(form.cleaned_data["email"]))
        for u in users:
            uid = urlsafe_base64_encode(force_bytes(u.pk))
            token = default_token_generator.make_token(u)
            url = self.request.build_absolute_uri(f"/reset/{uid}/{token}/")
            print("\n[password-reset url]", url, "\n")
        return super().form_valid(form)