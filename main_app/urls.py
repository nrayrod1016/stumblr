from django.urls import path
from . import views 

urlpatterns = [ 
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('posts/', views.posts_index, name='posts_index'),
  path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
]