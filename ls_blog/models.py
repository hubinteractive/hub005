from django.db import models

from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField


class PostCategory(models.Model):
    cat_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.cat_name 
    
    def get_absolute_url(self):
        # return reverse('blog:article-detail', args=(str(self.id)))
        return reverse('blog:index')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title_tag = models.CharField(max_length=255, default="My freakin' awesome blog")
    header_image =  models.ImageField(null=True, blank=True, upload_to="images/")
    body = models.TextField(null=True, blank=True)
    post_date = models.DateField(auto_now_add=True)
    cat_name = models.CharField(max_length=255, default='uncategorized')
    snippet = models.CharField(max_length=500)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    content = RichTextField(blank=True, null=True)
    

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('blog:article-detail', args=(str(self.id)))
        return reverse('blog:index')
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user) 