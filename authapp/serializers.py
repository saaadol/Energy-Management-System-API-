from rest_framework import serializers
from django.contrib.auth.models import User
from .models import * 

# User Serializer
# nom & prenom & list_dev



        
        
        
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields = ('id', 'username', 'email')

        
        
        
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
        
        
        
class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant 
        fields = '__all__'


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway 
        fields = '__all__'             


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device 
        fields = '__all__'       
  
class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = test 
        fields = '__all__'                   
                
       
        

             
                
