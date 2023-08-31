from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostCategory
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# def BaseIndex(request):  
#     context = {

#     }
  
#     return render(request, 'blog/index.html', context)

class BaseIndex(ListView):
    model =Post
    template_name = 'blog/index.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super(BaseIndex, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'
    def get_context_data(self, *args, **kwargs):
        
        cat_menu = PostCategory.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True 
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context



class AddPost(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostForm
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body')
    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super(AddPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UpdatePost(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = UpdatePostForm
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'body')
    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super(UpdatePost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:index')
    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super(DeletePost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
 

#  Categories

class AddCategory(CreateView):
    model = PostCategory
    template_name = 'blog/add_category.html'
    # form_class = PostForm
    fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body')
   
    

def CategoryView(request, cats):
    cat_posts = Post.objects.filter(cat_name=cats.replace('-', ' '))

    context = {
    'cats':cats.title().replace('-', ' '),
    'cat_posts':cat_posts,
    }
    return render(request, 'blog/category.html', context)

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id ).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('blog:article-detail', args=[str(pk)]))