from django.urls import path
from .views import ClientIndex





app_name = "edu"

urlpatterns = [
    path('', ClientIndex, name='edu-index'),
   
]