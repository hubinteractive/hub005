from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from members.models import Client
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404



# def ClientIndex(request):

#     context = {}

#     return render(request, 'client/client_index_list.html', context) 

# CLIENTS

class ClientListView(ListView):
    model = Client
    template_name = 'client/client_index_list.html'

class ClientProfilePage(DetailView):
    model = Client
    template_name = 'client/client_index_detail_test.html'
    def get_context_data(self, *args, **kwargs):
        clients = Client.objects.all()
        context = super(ClientProfilePage, self).get_context_data(*args, **kwargs)
        page_client = get_object_or_404(Client, id=self.kwargs['pk'])
        context["page_client"] = page_client
        return context
    

class ClientCreateView(CreateView):
    model = Client
    template_name = 'client/client_create.html'
    fields = '__all__'

# class ClientDetailView(DetailView):
#     model = Client
#     template_name = 'client/client_index_detail_test.html'
#     # template_name = 'client/client_details.html'

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