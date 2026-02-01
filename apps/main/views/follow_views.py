from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from apps.main.models import Follow
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_POST

@login_required
@require_POST
def follow_toggle(request, username):
    target_user = get_object_or_404(User, username=username)

    # 自分自身はフォローできない
    if request.user == target_user:
        return HttpResponseForbidden()

    follow_qs = Follow.objects.filter(
        follower=request.user,
        following=target_user
    )

    if follow_qs.exists():
        # アンフォロー
        follow_qs.delete()
    else:
        # フォロー
        Follow.objects.create(
            follower=request.user,
            following=target_user
        )

    return redirect(request.META.get("HTTP_REFERER", "profile:detail"))

def followers_list(request, username):
    user = get_object_or_404(User, username=username)
    followers = User.objects.filter(
        following__following=user
    )

    following_ids = []
    if request.user.is_authenticated:
        following_ids = Follow.objects.filter(
            follower=request.user
        ).values_list("following_id", flat=True)

    return render(request, "main/follow/followers_list.html", {
        "user_obj": user,
        "users": followers,
        "following_ids": following_ids,
    })

def following_list(request, username):
    user = get_object_or_404(User, username=username)
    following = User.objects.filter(
        followers__follower=user
    )

    following_ids = []
    if request.user.is_authenticated:
        following_ids = Follow.objects.filter(
            follower=request.user
        ).values_list("following_id", flat=True)

    return render(request, "main/follow/following_list.html", {
        "user_obj": user,
        "users": following,
        "following_ids": following_ids,
    })