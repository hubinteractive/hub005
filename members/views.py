from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from ls_blog.models import Post, PostCategory
from .models import ProfileInfo
from .forms import ProfileInfoForm



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
    template_name = 'registration/edit_profile.html'
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
    model = ProfileInfo
    template_name = 'profile/index.html'
    # ordering = ['-post_date']
    ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super(ProfileIndex, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class ProfileInfo(CreateView):
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