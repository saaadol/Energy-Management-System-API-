from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt


from django.views.generic import TemplateView

urlpatterns = [
   # Home & Login system URLS : 
   path('home',views.home,name='home'),
   path('signin',views.signin,name='signin'),
   path('signup',views.signup,name='signup'),
   #Plant Gateway
   path('plant',views.plant),
   path('show',views.show),
   path('update/<int:id>',views.update),
   path('edit/<int:id>',views.edit),
   path('delete/<int:id>',views.destroy),
   #Gateway URLS : 
   path('gateway',views.Gateway),
   path('showgateway',views.show_Gateway),
   path('updategateway/<int:id>',views.update_Gateway),
   path('editgateway/<int:id>',views.edit_Gateway),
   path('deletegateway/<int:id>',views.destroy_Gateway),
   #Device URLS:
   path('device',views.device),
   path('showdevice',views.show_Device),
   path('updatedevice/<int:id>',views.update_Device),
   path('editdevice/<int:id>',views.edit_Device),
   path('deletedevice/<int:id>',views.destroy_Device),
   #Rendering the gateway's device: 
   path('gatewaysdevice/<int:id>',views.gatewaysdevice),
   #Rendering data as json type : 
   path('plant_json',views.plant_json,name='plant_data'),
   path('gateway_json',views.gateway_json,name='Gateway_data'),
   path('device_json',views.device_json,name='Device_data')
   
   
   
   
   
   
]
   