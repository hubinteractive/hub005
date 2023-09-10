from django.contrib import admin

from .models import Post, PostCategory, Profile, Comment

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Profile)
admin.site.register(Comment)

# Register your models here.
