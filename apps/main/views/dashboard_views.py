from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from apps.main.models import Profile, ExercisePost
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden


@staff_member_required
def dashboard(request):
    return render(request, "main/dashboard/dashboard.html")

@staff_member_required
def user_list(request):
    users = User.objects.all().order_by("id")
    return render(request, "main/dashboard/user_list.html", {
        "users": users
    })

@staff_member_required
@staff_member_required
@require_POST
def user_toggle_active(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # 自分自身は変更不可（事故防止）
    if user == request.user:
        return HttpResponseForbidden("自分自身の状態は変更できません")

    user.is_active = not user.is_active
    user.save()

    return redirect("dashboard:user_detail", user_id=user.id)

@staff_member_required
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = Profile.objects.get(user=user)

    return render(request, "main/dashboard/user_detail.html", {
        "user_obj": user,
        "profile": profile,
    })

@staff_member_required
def post_list(request):
    posts = ExercisePost.objects.all().order_by("-created_at")
    return render(request, "main/dashboard/post_list.html", {
        "posts": posts
    })

@staff_member_required
def post_delete_confirm(request, post_id):
    post = get_object_or_404(ExercisePost, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect("dashboard:post_list")

    return render(request, "main/dashboard/post_delete_confirm.html", {
        "post": post
    })