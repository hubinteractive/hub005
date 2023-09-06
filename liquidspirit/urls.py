from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ls_blog.urls', namespace='blog')),
    path('members/', include('django.contrib.auth.urls',)),
    path('members/', include('members.urls', namespace='members')),
    path('education/', include('edu.urls', namespace='edu')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
