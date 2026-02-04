from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.common.api.health import healthz
from apps.main.views.top_views import top  # LP用view

urlpatterns = [
    # トップページ（LP）
    path("", top, name="top"),

    path("admin/", admin.site.urls),
    path("healthz/", healthz),

    # 認証
    path("auth/", include("apps.main.urls.auth_urls")),

    # 投稿
    path("post/", include("apps.main.urls.post_urls")),
    path("post/", include("apps.main.urls.search_urls")),

    # プロフィール
    path("profile/", include("apps.main.urls.profile_urls")),

    # フォロー
    path("follow/", include("apps.main.urls.follow_urls")),

    # いいね
    path("reaction/", include("apps.main.urls.reaction_urls")),

    # 管理画面
    path("dashboard/", include(("apps.main.urls.dashboard_urls", "dashboard"))),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
