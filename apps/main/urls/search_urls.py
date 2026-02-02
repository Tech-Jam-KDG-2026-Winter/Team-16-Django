# apps/main/urls/search_urls.py
from django.urls import path
from apps.main.views import search_views

app_name = "search"

urlpatterns = [
    path("search/", search_views.post_search, name="search"),
    path("sort/", search_views.post_sort, name="sort"),
]
