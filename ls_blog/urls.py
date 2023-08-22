from django.urls import path
# from . import views 

from .views import BaseIndex, ArticleDetailView, AddPost, UpdatePost, DeletePost, AddCategory, CategoryView, LikeView


app_name = 'blog'

urlpatterns = [


    # path('', views.BaseIndex, name='index'),
    path('', BaseIndex.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPost.as_view(), name='add-post'),
    path('article/update/<int:pk>', UpdatePost.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePost.as_view(), name='delete-post'),
    path('add_category/', AddCategory.as_view(), name='add-category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like-post'),

    
    
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('services/', views.services, name='services'),
    # path('services/custom_software_development/', views.custom_software_development, name='cs-development'),
    # path('services/custom_software_development/product_design', views.product_design, name='product-design'),
    # path('services/custom_software_development/software_architecture', views.software_architecture, name='software-architecture'),
    # path('services/custom_software_development/web_development', views.web_development, name='web-development'),
    # path('services/custom_software_development/mobile_development', views.mobile_development, name='mobile-development'),
    # path('services/custom_software_development/support_maintenance', views.support_maintenance, name='support-maintenance'),
    # path('services/custom_software_development/quality', views.quality, name='quality'),
    # path('services/custom_software_development/approach', views.approach, name='approach'),
    # path('company_info', views.companyInfo, name='company-info'),
    # path('marketing', views.marketing, name='marketing'),
    # path('framework', views.framework, name='framework'),
    # path('brands', views.brands, name='brands'),
]