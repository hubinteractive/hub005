from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy


# def BaseIndex(request):  
#     context = {

#     }
  
#     return render(request, 'blog/index.html', context)

class BaseIndex(ListView):
    model =Post
    template_name = 'blog/index.html'
    ordering = ['-post_date']
    # ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'



class AddPost(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostForm
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body')


class UpdatePost(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = UpdatePostForm
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'body')


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:index')
 