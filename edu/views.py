from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect



def ClientIndex(request):

    context = {}

    return render(request, 'education/edu_index.html', context) 
