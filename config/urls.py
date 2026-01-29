from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from apps.common.api.health import healthz
from django.conf import settings
from django.conf.urls.static import static


def root(request):
    return JsonResponse({"service": "django-starter", "status": "ok"})

urlpatterns = [
    path("",root),
    path("admin/", admin.site.urls),
    path("healthz/", healthz),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )