from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from apps.common.api.health import healthz

def root(request):
    return JsonResponse({"service": "django-starter", "status": "ok"})

urlpatterns = [
    path("",root),
    path("admin/", admin.site.urls),
    path("healthz/", healthz),
    #投稿
    path("post/", include("apps.main.urls.post_urls")),
    # 追加：ログイン/ログアウト
    path("", include("apps.main.urls.auth_urls")),
]
