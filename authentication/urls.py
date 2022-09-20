
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('hotel/', views.display_hotel_images, name='hotel_images'),
    path('followers_count/<int:id>/',views.followers_count,name='followers_count'),
    path('unfollowers_count/<int:id>/',views.followers_count,name='unfollowers_count'),
    path('register/', views.register, name='register'),
    path('add_detail', views.emp,name='add_detail'),
    path('hot/<int:id>/', views.like, name='hot'),
    path('n_not/<int:id>/', views.dislike, name='n_not'),

]