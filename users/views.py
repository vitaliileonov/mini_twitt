from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from users.forms import UserForm
from posts.models import Posts, Comment

def user_list(request):
    users = User.objects.all()
    context = {'users': users, 'title': 'User list'}
    return render(request, 'users/users.html', context)

def user_detail(request, username):

    user = get_object_or_404(User, username=username)
    posts = Posts.objects.filter(user__id=user.pk)
    comments = Comment.objects.filter(user__id=user.pk)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)  # Використовуйте існуючий об'єкт користувача
        if form.is_valid():
            form.save()  # Зберігає оновлені дані користувача
            return redirect('user_detail', username=username)
    else:
        form = UserForm(instance=user)  # Відображення форми з поточними даними користувача

    context = {
        'user': user,
        'posts': posts,
        'comments': comments,
        'form': form,
         }
    return render(request, 'users/user.html', context)

# def create_profile(request, username):
#
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         profile = form.save(commit=False)
#         profile.username = username
#         profile.save()
