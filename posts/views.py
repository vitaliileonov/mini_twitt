from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Posts, Comment
from posts.forms import PostForm, CommentForm

def posts(request):
    posts = Posts.objects.all()
    user = request.GET.get("user", "all")
    form = PostForm()
    context = {
        'posts': posts,
        'user': user,
        'form': form,
             }
    return render(request, 'posts/post.html', context)


def comment(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    comment = Comment.objects.filter(post__id=post_id)
    context = {'comment': comment, 'title': 'Comment list'}
    return render(request, 'posts/comment.html', context)

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('posts')

    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

def post_detail(request, post_id):

    post = get_object_or_404(Posts, pk=post_id)
    comments = Comment.objects.filter(post__id=post_id)
    form = CommentForm(request.POST or None)
    print(post)
    if request.method == 'POST':
        if form.is_valid():
            add_comment(request, post)  # Виклик функції для збереження коментаря
            return redirect('post_detail', post_id=post_id)

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'posts/post_detail.html', context)

def add_comment(request, post_id):

    form = CommentForm(request.POST or None)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post = post_id
        new_comment.save()
