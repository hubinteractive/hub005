from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from ls_blog.models import Post, PostCategory
from members.models import ProfileInfo, Client
from .forms import ProfileInfoForm, ProfileUpdateForm, ProfileCreteForm
from django.http import HttpResponseRedirect




class MembersRegisterView(generic.CreateView):
    form_class =SignUpForm
    template_name = 'registration/register.html'
    success_url =reverse_lazy('login')



class MembersLoginView(generic.CreateView):
    form_class =UserCreationForm
    template_name = 'registration/login.html'
    success_url =reverse_lazy('index')


class MembersEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'profile/edit_profile.html'
    success_url =reverse_lazy('blog:index')

    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url =reverse_lazy('members:password-success')

def PasswordSucces(request):
    context = {

    }
    return render(request, 'registration/password_success.html', context)




class ProfileIndex(ListView):
    model = Client
    template_name = 'profile/profile_index.html'

    # ordering = ['-post_date']
    # ordering = ['-id']
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = PostCategory.objects.all()
    #     context = super(ProfileIndex, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context
class ProfileDetailView(DetailView):
    model = ProfileInfo
    template_name = 'profile/profile_details.html'



# class PIndex(ListView):
#     model = ProfileInfo
#     template_name = 'profile/index.html'
#     # ordering = ['-post_date']
#     # ordering = ['-id']
#     # def get_context_data(self, *args, **kwargs):
#     #     cat_menu = PostCategory.objects.all()
#     #     context = super(ProfileIndex, self).get_context_data(*args, **kwargs)
#     #     context["cat_men
    
class ProfileInfo(ListView):
    model = ProfileInfo
    template_name = 'profile/info_profile.html'
    form_class = ProfileInfoForm
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body')
    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super(ProfileInfo, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ProfileCreateView(CreateView):
    model = Post
    template_name = 'profile/profile_create.html'
    form_class = ProfileUpdateForm
    # fields = '__all__'
    # fields = ('title', 'title_tag', 'author', 'body')
    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super(ProfileCreateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

class ProfileUpdate(UpdateView):
    model = ProfileInfo
   
    # form_class = ProfileUpdateForm
    template_name = 'profile/update_profile.html'
    # fields = '__all__'
    fields = ('bio', 'website_url', 'facebook_url')

    


  

    
class ProfileDelete(DeleteView):
    model = ProfileInfo
    template_name = 'profile/delete_profile.html'
    success_url = reverse_lazy('blog:index')
    

    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super(ProfileDelete, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    


    