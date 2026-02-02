from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from apps.main.models import ExercisePost,Reaction

@login_required
def like_post(request,post_id):
  post = get_object_or_404(ExercisePost, id = post_id)

  Reaction.objects.get_or_create(
    user = request.user,
    post = post
  )

  return redirect(request.META.get("HTTP_REFERER","post_list"))


@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(ExercisePost, id=post_id)

    Reaction.objects.filter(
        user=request.user,
        post=post
    ).delete()

    return redirect(request.META.get("HTTP_REFERER", "post_list"))