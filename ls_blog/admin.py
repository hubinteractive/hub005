from django.contrib import admin

from .models import Post, PostCategory, Profile

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Profile)

# Register your models here.
