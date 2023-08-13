from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post 


# def BaseIndex(request):  
#     context = {

#     }
  
#     return render(request, 'blog/index.html', context)

class BaseIndex(ListView):
    model =Post
    template_name = 'blog/index.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'