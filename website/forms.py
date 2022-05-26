from django import forms
from django.forms import fields
from website.models import new_Plant,new_Gateway,new_Device 

class PlantForm(forms.ModelForm):
    class Meta:    
        model=new_Plant
        fields="__all__"

class GatewayForm(forms.ModelForm):
    class Meta:    
        model=new_Gateway
        fields="__all__"


class DeviceForm(forms.ModelForm):
    class Meta:    
        model=new_Device
        fields="__all__"                    