from django.urls import path
from .views import MembersRegisterView, MembersLoginView

app_name = 'members'

urlpatterns = [
    path('register/', MembersRegisterView.as_view(), name='register'),
    path('login/', MembersLoginView.as_view(), name='login'),

    # path('', views.BaseIndex, name='index'),
    # path('', BaseIndex.as_view(), name='index'),
    # path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    # path('add_post/', AddPost.as_view(), name='add-post'),
    # path('article/update/<int:pk>', UpdatePost.as_view(), name='update-post'),
    # path('article/<int:pk>/delete', DeletePost.as_view(), name='delete-post'),

]