from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ls_blog.urls', namespace='blog')),
]
