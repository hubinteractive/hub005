from django.urls import path
from .views import MembersRegisterView, MembersLoginView, MembersEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from .views import PasswordSucces

app_name = 'members'

urlpatterns = [
    path('signup/register/', MembersRegisterView.as_view(), name='register'),
    # path('register/signup', MembersRegisterView.as_view(), name='signup'),
    path('login/', MembersLoginView.as_view(), name='login'),
    path('edit_profile/', MembersEditView.as_view(), name='edit-profile'),
    # path('password/', auth_views.PasswordChangeView.as_view()),

    path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html'), name='change-password'),
   
    path('password_success/', PasswordSucces, name='password-success')


]

