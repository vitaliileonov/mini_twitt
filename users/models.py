from django.db import models
from django.utils import timezone

class User(models.Model):

    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateField(default=timezone.now)
    profile_picture = models.ImageField(upload_to="users/profile_images", null=True, blank=True)
    title_picture = models.ImageField(upload_to="users/title_images", null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     # Якщо поле 'name' порожнє, встановіть його значення на основі 'username'
    #     if not self.name:
    #         self.name = self.username
    #     super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f'User: {self.username} {self.email}'
