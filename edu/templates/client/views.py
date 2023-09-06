from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from members.models import Client
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404



def EducationIndex(request):

    context = {}

    return render(request, 'edutmp/edu_index.html', context) 

# CLIENTS

class ClientListView(ListView):
    model = Client
    template_name = 'edutmp/client_list.html'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'client/client_create.html'
    fields = '__all__'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client/client_details.html'

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client/client_update.html'
    fields = '__all__'

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('blog:index')
    
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = PostCategory.objects.all()
    #     context = super(ProfileDelete, self).get_context_data(*args, **kwargs)
    #     context["cat_menu"] = cat_menu
    #     return context