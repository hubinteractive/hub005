from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm



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
    form_class = PasswordChangeForm
    success_url =reverse_lazy('login')