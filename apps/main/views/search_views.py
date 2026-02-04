# apps/main/views/search_views.py
from django.shortcuts import render
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required

from apps.main.models import ExercisePost, Reaction, Follow


@login_required
def post_search(request):
    query = request.GET.get("q", "")

    posts = ExercisePost.objects.annotate(
        like_count=Count("reactions")
    )

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    liked_post_ids = Reaction.objects.filter(
        user=request.user
    ).values_list("post_id", flat=True)

    return render(request, "main/post/list.html", {
        "posts": posts,
        "liked_post_ids": liked_post_ids,
        "query": query,
    })


@login_required
def post_sort(request):
    sort = request.GET.get("sort", "new")

    posts = ExercisePost.objects.annotate(
        like_count=Count("reactions")
    )

    if sort == "like":
        posts = posts.order_by("-like_count", "-created_at")
    elif sort == "follow":
        following_users = Follow.objects.filter(
            follower=request.user
        ).values_list("following", flat=True)
        posts = posts.filter(user__in=following_users)
    else:
        posts = posts.order_by("-created_at")

    liked_post_ids = Reaction.objects.filter(
        user=request.user
    ).values_list("post_id", flat=True)

    return render(request, "main/post/list.html", {
        "posts": posts,
        "liked_post_ids": liked_post_ids,
        "sort": sort,
    })
