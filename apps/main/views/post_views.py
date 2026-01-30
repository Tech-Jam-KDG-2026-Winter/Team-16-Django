from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from ..models import ExercisePost


#投稿作成
@login_required
def post_create(request):
  if request.method == 'POST':
    ExercisePost.objects.create(
      user = request.user,
      title = request.POST['title'],
      content = request.POST['content'],
      duration = request.POST['duration'],
    )
    return redirect('post_list')
  return render(request, 'post/create.html')


#投稿一覧
@login_required
def post_list(request):
  posts = ExercisePost.objects.select_related('user').order_by('-created_at')
  return render(request, 'post/list.html', {
    'posts' : posts
  })


#投稿詳細
@login_required
def post_detail(request,post_id):
  post = get_object_or_404(ExercisePost, id=post_id)
  return render(request, 'post/detail.html',{
    'post' : post
  })


#投稿編集
@login_required
def post_edit(request, post_id):
  post = get_object_or_404(ExercisePost, id = post_id) 

  if post.user != request.user:
    return request('post_detail',post_id = post.id) 
  
  if request.method == 'POST':
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.duration = request.POST['duration']
    post.save()
    return redirect('post_detail',post_id = post.id)
  
  return render(request,'post//edit.html',{
    'post' : post
  })


#投稿削除
@login_required
def post_delete(request, post_id):
  post = get_object_or_404(ExercisePost, id = post_id)

  if post.user == request.user and request.method == 'POST':
    post.delete()

    return redirect('post_list')
  