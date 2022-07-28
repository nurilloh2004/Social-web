from django.urls import re_path
from . import views

app_name = 'images'

urlpatterns = [
    re_path('create/', views.image_create, name='create'),
    re_path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    re_path('like/', views.image_like, name='like'),
    re_path('', views.image_list, name='list'),
    re_path('ranking/', views.image_ranking, name='ranking'),
]