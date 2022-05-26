
from django.contrib import admin
from django.urls import path,include
from knox import views as knox_views
from rest_framework.decorators import api_view
from . import views


urlpatterns = [
    
    path('',views.RegisterAPI.as_view(), name='User-register'),
    path('user-login',views.LoginAPI.as_view(), name='User-login'),
    path('user-logout',knox_views.LogoutView.as_view(), name='User-logout'),
    
    
    
    
    path('plant-api',views.Plant_API, name='Plant-api'),
    path('plant-detail/<str:key>/',views.Plant_Detail, name='Plant-Detail'),
    path('plant-update/<str:key>/',views.Plant_Update, name='Plant-Update'),
    path('plant-delete/<str:key>/',views.Plant_Delete, name='Plant-Delete'),
    
    #Gateway URLs : 
    
    path('gateway-api',views.Gateway_API, name='GATEWAY-api'),
    path('gateway-detail/<str:key>/',views.Gateway_Detail, name='GATEWAY-Detail'),
    path('gateway-update/<str:key>/',views.Gateway_Update, name='GATEWAY-Update'),
    path('gateway-delete/<str:key>/',views.Gateway_Delete, name='GATEWAY-Delete'),
    
    #Device URLs : 
    
    path('device-api',views.Device_API, name='GATEWAY-api'),
    path('device-detail/<str:key>/',views.Device_Detail, name='DEVICE-Detail'),
    path('device-update/<str:key>/',views.Device_Update, name='DEVICE-Update'),
    path('device-delete/<str:key>/',views.Device_Delete, name='DEVICE-Delete'),
    
    #test URLS : 
    path('test-api',views.test_API, name='test-api'),
    path('test-detail/<str:key>/',views.test_Detail, name='test-Detail'),
    path('test-update/<str:key>/',views.test_Update, name='test-Update'),
    path('test-delete/<str:key>/',views.test_Delete, name='test-Delete'),
    
    
    
    
]