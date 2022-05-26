from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .models import *
from .serializers import *  
from rest_framework.decorators import api_view
from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

# Register API
"""
@api_view(['GET','POST'])
def User_API(request):
    if request.method=="POST":
        data=request.data
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors) 
            return Response({'status':403,'errors':serializer.errors,'message':'Something wrong'})
        serializer.save()
        return Response({'status':200,'payload':data,'message':'Done'})
        
    User_objs=User_Data.objects.all()
    serializer=UserSerializer(User_objs,many=True)
    return Response({'status':200,'payload':serializer.data})
"""
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
        
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)   
        
        
@api_view(['GET','POST'])
def Plant_API(request):
    if request.method=="POST":
        data=request.data
        serializer=PlantSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors) 
            return Response({'status':403,'errors':serializer.errors,'message':'Something wrong'})
        serializer.save()
        return Response({'status':200,'payload':data,'message':'Done'})
        
    Plant_objs=Plant.objects.all()
    serializer=PlantSerializer(Plant_objs,many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['GET'])
def Plant_Detail(request,key):
    plant=Plant.objects.get(id=key)
    serializer=PlantSerializer(plant,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Plant_Update(request,key):
    plant=Plant.objects.get(id=key)
    serializer=PlantSerializer(instance=plant,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':200,'message':'Done Updating'})


@api_view(['DELETE'])
def Plant_Delete(request,key):
    plant=Plant.objects.get(id=key)
    plant.delete()
    return Response({'status':200,'message':'Done Deleting'})



##### Gateway API :

@api_view(['GET','POST'])
def Gateway_API(request):
    if request.method=="POST":
        data=request.data
        serializer=GatewaySerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors) 
            return Response({'status':403,'errors':serializer.errors,'message':'Something wrong'})
        serializer.save()
        return Response({'status':200,'payload':data,'message':'Done'})
        
    Gateway_objs=Gateway.objects.all()
    serializer=GatewaySerializer(Gateway_objs,many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['GET'])
def Gateway_Detail(request,key):
    gateway=Gateway.objects.get(id=key)
    serializer=GatewaySerializer(gateway,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Gateway_Update(request,key):
    gateway=Gateway.objects.get(id=key)
    serializer=GatewaySerializer(instance=gateway,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':200,'message':'Done Updating'})


@api_view(['DELETE'])
def Gateway_Delete(request,key):
    gateway=Gateway.objects.get(id=key)
    gateway.delete()
    return Response({'status':200,'message':'Done Deleting'})


#### Device API : 


@api_view(['GET','POST'])
def Device_API(request):
    if request.method=="POST":
        data=request.data
        serializer=DeviceSerializer(data=request.data)
        if not serializer.is_valid():
            #print(serializer.errors) 
            return Response({'status':403,'errors':serializer.errors,'message':'Something wrong'})
        serializer.save()
        return Response({'status':200,'payload':data,'message':'Done'})
        
    Device_objs=Device.objects.all()
    serializer=DeviceSerializer(Device_objs,many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['GET'])
def Device_Detail(request,key):
    device=Device.objects.get(id=key)
    serializer=DeviceSerializer(device,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Device_Update(request,key):
    device=Device.objects.get(id=key)
    serializer=DeviceSerializer(instance=device,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':200,'message':'Done Updating'})


@api_view(['DELETE'])
def Device_Delete(request,key):
    device=Device.objects.get(id=key)
    device.delete()
    return Response({'status':200,'message':'Done Deleting'})
    
    
    
    
#### test API : 


@api_view(['GET','POST'])
def test_API(request):
    if request.method=="POST":
        data=request.data
        serializer=testSerializer(data=request.data)
        if not serializer.is_valid():
            #print(serializer.errors) 
            return Response({'status':403,'errors':serializer.errors,'message':'Something wrong'})
        serializer.save()
        return Response({'status':200,'payload':data,'message':'Done'})
        
    test_objs=test.objects.all()
    serializer=testSerializer(test_objs,many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['GET'])
def test_Detail(request,key):
    Test=test.objects.get(id=key)
    serializer=testSerializer(Test,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def test_Update(request,key):
    Test=test.objects.get(id=key)
    serializer=testSerializer(instance=Test,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':200,'message':'Done Updating'})


@api_view(['DELETE'])
def test_Delete(request,key):
    Test=test.objects.get(id=key)
    Test.delete()
    return Response({'status':200,'message':'Done Deleting'})
        
    
    
    
    
    
    
    
    

