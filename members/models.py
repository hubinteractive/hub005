from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ProfileInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic =  models.ImageField(null=True, blank=True, upload_to="images/profile")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user) 
    
    def get_absolute_url(self):
        # return reverse('blog:article-detail', args=(str(self.id)))
        return reverse('members:index')
    
class Client(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(default='No bio')
    profile_pic =  models.ImageField(null=True, blank=True, upload_to="images/profile")
    website_url = models.CharField(max_length=255, null=True, blank=True, default='https://')
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user) 
    
    def get_absolute_url(self):
        return reverse('members:client-profile-details-page', args=(str(self.id)))
        # return reverse('members:index')
