from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from apps.main.models import Profile, ExercisePost

@staff_member_required
def dashboard(request):
    return render(request, "admin/dashboard.html")

@staff_member_required
def user_list(request):
    users = User.objects.all().order_by("id")
    return render(request, "admin/user_list.html", {
        "users": users
    })

@staff_member_required
def user_toggle_active(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = not user.is_active
    user.save()
    return redirect("admin:user_list")

@staff_member_required
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = user.profile

    if request.method == "POST":
        profile.is_banned = True
        profile.save()
        return redirect("admin:user_list")

    return render(request, "admin/user_detail.html", {
        "user_obj": user,
        "profile": profile,
    })

@staff_member_required
def post_list(request):
    posts = ExercisePost.objects.all().order_by("-created_at")
    return render(request, "admin/post_list.html", {
        "posts": posts
    })

@staff_member_required
def post_delete_confirm(request, post_id):
    post = get_object_or_404(ExercisePost, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect("admin:post_list")

    return render(request, "admin/post_delete_confirm.html", {
        "post": post
    })