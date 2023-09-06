from django.urls import path
from .views import MembersRegisterView, MembersLoginView, MembersEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from .views import PasswordSucces, ProfileIndex, ProfileInfo, ProfileUpdate, ProfileDelete,  ProfileCreateView, ProfileDetailView

app_name = 'members'

urlpatterns = [
    path('', ProfileIndex.as_view(), name='index'),
    # path('', PIndex.as_view(), name='index'),
    path('info_profile/', ProfileInfo.as_view(), name='info_profile'),
    path('<int:pk>/update-profile', ProfileUpdate.as_view(), name='update-profile'),
    path('profile/<int:pk>/delete', ProfileDelete.as_view(), name='delete-profile'),
    path('create_profile', ProfileCreateView.as_view(), name='create-profile'),
    path('profile/detail/<int:pk>', ProfileDetailView.as_view(), name='profile-detail'),
    # path('profile/<int:pk>', ProfileIndex.as_view(), name='index'),


    path('signup/register/', MembersRegisterView.as_view(), name='register'),
    # path('register/signup', MembersRegisterView.as_view(), name='signup'),
    path('login/', MembersLoginView.as_view(), name='login'),
    path('edit_profile/', MembersEditView.as_view(), name='edit-profile'),
    # path('password/', auth_views.PasswordChangeView.as_view()),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html'), name='change-password'),
    path('password_success/', PasswordSucces, name='password-success'),


]

