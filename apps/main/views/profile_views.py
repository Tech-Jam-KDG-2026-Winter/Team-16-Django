from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden

from django.contrib.auth.models import User
from apps.main.models import Profile
from apps.main.forms.profile_forms import ProfileForm


def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    profile, _ = Profile.objects.get_or_create(user=user)

    return render(request, "main/profile/detail.html", {
        "profile_user": user,
        "profile": profile,
    })


@login_required
def profile_edit(request):
    """
    ★ ここが直リンク対策の本丸
    編集できるのは request.user の Profile のみ
    """
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile:detail", username=request.user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, "main/profile/edit.html", {
        "form": form,
    })


@login_required
def profile_delete(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("login")