from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from apps.main.models import ExercisePost, Follow, Reaction


# 投稿作成
@login_required
def post_create(request):
    if request.method == 'POST':
        ExercisePost.objects.create(
            user=request.user,
            title=request.POST['title'],
            content=request.POST['content'],
            duration=request.POST['duration'],
        )
        return redirect('post_list')

    return render(request, 'main/post/create.html')


# 投稿一覧
@login_required
def post_list(request):
    posts = ExercisePost.objects.select_related('user').annotate(
        like_count=Count("reactions")
    ).order_by('-created_at')

    liked_post_ids = Reaction.objects.filter(
        user=request.user
    ).values_list("post_id", flat=True)

    return render(request, 'main/post/list.html', {
        'posts': posts,
        'liked_post_ids': liked_post_ids,
    })


# 投稿詳細
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(
        ExercisePost.objects.annotate(
            like_count=Count("reactions")
        ),
        id=post_id
    )

    # フォロー判定
    is_following = False
    if request.user != post.user:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=post.user
        ).exists()

    # いいね判定
    is_liked = Reaction.objects.filter(
        user=request.user,
        post=post
    ).exists()

    return render(request, 'main/post/detail.html', {
        'post': post,
        'is_following': is_following,
        'is_liked': is_liked,
    })


# 投稿編集
@login_required
def post_edit(request, post_id):
    post = get_object_or_404(ExercisePost, id=post_id)

    if post.user != request.user:
        return redirect('post_detail', post_id=post.id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.duration = request.POST['duration']
        post.save()
        return redirect('post_detail', post_id=post.id)

    return render(request, 'main/post/edit.html', {
        'post': post
    })


# 投稿削除
@login_required
def post_delete(request, post_id):
    post = get_object_or_404(ExercisePost, id=post_id)

    if request.method == 'POST' and post.user == request.user:
        post.delete()

    return redirect('post_list')
