from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_all, name='post_list_all'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('author/<pk>/', views.post_list_blogger, name='post_list_blogger'),
    path('author/<pk>/fav/add', views.add_favorite_blogger, name='add_favorite_blogger'),
    path('author/<pk>/fav/del', views.del_favorite_blogger, name='del_favorite_blogger'),
]
