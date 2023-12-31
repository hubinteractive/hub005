from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ClientForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from ls_blog.models import Post, PostCategory
from members.models import ProfileInfo, Client
from .forms import ProfileInfoForm, ProfileUpdateForm, ProfileCreteForm
from django.http import HttpResponseRedirect
from django.urls import reverse




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



# Client
# class ClientIndexView(ListView):
#     model = User
#     template_name = 'client/client_index_list.html'

#     # ordering = ['-post_date']
#     # ordering = ['-id']
#     # def get_context_data(self, *args, **kwargs):
#     #     cat_menu = PostCategory.objects.all()
#     #     context = super(ProfileIndex, self).get_context_data(*args, **kwargs)
#     #     context["cat_menu"] = cat_menu    
#     #     return context

class ProfileView(DeleteView):
    model = User
    template_name = 'profile/profile_view.html'
    def get_context_data(self, *args, **kwargs):
        clients = User.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_client = get_object_or_404(User, id=self.kwargs['pk'])
        context["page_client"] = page_client 
        context["clients"] = clients 
        return context

class ClientProfilePage(DetailView):
    model = Client
    template_name = 'profile/index.html'
    def get_context_data(self, *args, **kwargs):
        clients = Client.objects.all()
        context = super(ClientProfilePage, self).get_context_data(*args, **kwargs)
        page_client = get_object_or_404(Client, id=self.kwargs['pk'])
        context["page_client"] = page_client 
        context["clients"] = clients 
        return context
    

class ClientListView(ListView):
    model = Client
    template_name = 'client/client_index_list.html'
    ordering = ['-id']



    
class ClientCreateView(CreateView):
    model = Client
    template_name = 'client/client_create.html'
    form_class =ClientForm
    success_url = reverse_lazy('members:all-client-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     return reverse('members:view-profile', kwargs={'id': self.object.id})


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client/client_update.html'
    form_class =ClientForm
    success_url = reverse_lazy('members:all-client-list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('members:all-client-list')
   
    # def get_success_url(self):
    #     return reverse('members:view-profile', kwargs={'pk': self.object.pk})
        
    
 

    # ProfileInfo
class ProfileInfo(ListView):
    model = Client
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
    model = Client
   
    # form_class = ProfileUpdateForm
    template_name = 'profile/update_profile.html'
    # fields = '__all__'
    fields = ('bio', 'website_url', 'facebook_url')

    
class ProfileDelete(DeleteView):
    model = Client
    template_name = 'profile/delete_profile.html'
    success_url = reverse_lazy('blog:index')
    

    def get_context_data(self, *args, **kwargs):
        cat_menu = PostCategory.objects.all()
        context = super(ProfileDelete, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    


    