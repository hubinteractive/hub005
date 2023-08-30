from django import forms
from django.contrib import admin
from .models import Post, PostCategory
from ckeditor.widgets import CKEditorWidget

choices = PostCategory.objects.all().values_list('cat_name', 'cat_name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'content', 'cat_name', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),  
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),  
            'author': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id': 'sneks', 'type':'hidden'}), 
            # 'author': forms.Select(attrs={'class':'form-control'}),  
            'cat_name': forms.Select(choices=choice_list, attrs={'class':'form-control'}),  
            'body': forms.Textarea(attrs={'class':'form-control'}),  
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'cat_name',  'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control',  'placeholder':'This is title placeholder',}),  
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),  
            'cat_name': forms.Select(choices=choice_list, attrs={'class':'form-control'}),  
            # 'author': forms.Select(attrs={'class':'form-control'}),  
            'body': forms.Textarea(attrs={'class':'form-control'}),  
        }