from django.urls import path
from . import views

urlpatterns = [
    path('get_media_info/', views.get_media_info, name='get_media_info'),
    path('', views.index, name='index'),
]
