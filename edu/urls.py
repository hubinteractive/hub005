from django.urls import path
# from .views import EducationIndex
from .views import ClientCreateView, ClientDeleteView, ClientUpdateView,  ClientListView, ClientProfilePage




app_name = "edu"

urlpatterns = [
    # path('', ClientIndex, name='edu-index'),
        # CLIENT
    path('', ClientListView.as_view(), name='client-list' ),
    path('clients/client_create',ClientCreateView.as_view(), name='client-create' ),

    # path('client_details/<int:pk>', ClientDetailView.as_view(), name='client-details'),
    path('<int:pk>/client_profile_details_page', ClientProfilePage.as_view(), name='client-profile-details-page'),

    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='client-update'),
    path('client_delete/<int:pk>/delete', ClientDeleteView.as_view(), name='client-delete'),
]