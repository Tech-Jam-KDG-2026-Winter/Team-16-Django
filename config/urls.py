from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from apps.common.api.health import healthz
from django.conf import settings
from django.conf.urls.static import static


def root(request):
    return JsonResponse({"service": "django-starter", "status": "ok"})


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


