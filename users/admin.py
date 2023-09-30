from django.contrib import admin

from users.models import User
from posts.models import Posts, Comment

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Comment)

# Register your models here.
