from django.db import models
from users.models import User

class Posts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.CharField(max_length=128)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return f'Posts: {self.user} {self.content}'


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return f'Comment: {self.user} {self.post} {self.content}'
