"""MyBlog URL configuration"""

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]