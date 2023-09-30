from django.urls import path
from .views import posts, comment, add_post, post_detail, add_comment
urlpatterns = [
    path('', posts, name="posts"),
    path('post/', add_post, name="add_post"),
    path('post/<int:post_id>', post_detail, name="post_detail"),
    # path('comment/<int:post_id>', comment, name="comment"),
    path('add-comment/<int:post_id>', add_comment, name='add_comment')
]
