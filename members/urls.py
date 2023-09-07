from django.urls import path
from .views import MembersRegisterView, MembersLoginView, MembersEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from .views import PasswordSucces, ProfileInfo, ClientProfilePage, ClientListView, ClientUpdateView, ClientDeleteView, ClientCreateView # ClientIndexView 
from .views import ProfileDelete,ProfileDelete, ProfileUpdate, ProfileCreateView

app_name = 'members'

urlpatterns = [
    # path('', ClientIndexView.as_view(), name='index'),



    path('profile/<int:pk>/delete', ProfileDelete.as_view(), name='delete-profile'),
    path(' ', ProfileInfo.as_view(), name='info_profile'),
    # path('<int:pk>/update-profile', ProfileUpdate.as_view(), name='update-profile'),
  
    path('create_profile', ProfileCreateView.as_view(), name='create-profile'),
    



    # Client
    path('clients_all', ClientListView.as_view(), name='all-client-list' ),

    path('<int:pk>/client_profile_details_page', ClientProfilePage.as_view(), name='client-profile-details-page'),


    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='client-update'),
    path('client_delete/<int:pk>/delete', ClientDeleteView.as_view(), name='client-delete'),
    path('clients/client_create',ClientCreateView.as_view(), name='client-create' ),



    # Register
    path('signup/register/', MembersRegisterView.as_view(), name='register'),
    # path('register/signup', MembersRegisterView.as_view(), name='signup'),
    path('login/', MembersLoginView.as_view(), name='login'),
    path('edit_profile/', MembersEditView.as_view(), name='edit-profile'),
    # path('password/', auth_views.PasswordChangeView.as_view()),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html'), name='change-password'),
    path('password_success/', PasswordSucces, name='password-success'),


]

