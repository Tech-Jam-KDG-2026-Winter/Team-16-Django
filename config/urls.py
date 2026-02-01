from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from apps.common.api.health import healthz




def root(request):
    # 未ログインならログインへ、ログイン済みなら投稿一覧へ
    if request.user.is_authenticated:
        return redirect("/post/")
    return redirect("login")  # auth_urls.py の name="login" を参照


urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
    path("healthz/", healthz),

    # 認証
    path("", include("apps.main.urls.auth_urls")),

    # 投稿
    path("post/", include("apps.main.urls.post_urls")),

    # プロフィール
    path("profile/", include("apps.main.urls.profile_urls")),

    # 管理画面（独自）
    path("dashboard/",include(("apps.main.urls.dashboard_urls", "dashboard")),),

    ]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    #投稿
    path("post/", include("apps.main.urls.post_urls")),
    # 追加：ログイン/ログアウト
    path("", include("apps.main.urls.auth_urls")),


