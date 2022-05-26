from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from website.models import new_Plant,new_Gateway,new_Device
from website.forms import PlantForm,GatewayForm,DeviceForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 
@csrf_exempt
# Create your views here.
def home(request):
	return render(request,"website/hello.html")




def signup(request):

	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('signin')	
	else:
		form=UserCreationForm()
		



	return render(request,"website/signup.html",{'form':form})



def signin(request):
	
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			return redirect('/show')

	else:
		form=AuthenticationForm()

	return render(request,"website/signin.html",{'form':form})

def plant(request):
	if request.method=="POST":
		form=PlantForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/show')
			except:
				pass
	else:
		form=PlantForm()
	return render(request,'index.html',{'form':form})
		
def show(request):
    plants=new_Plant.objects.all()
    return render(request,'website/show.html',{'plants':plants})		

def edit(request,id):
    plant=new_Plant.objects.get(id=id)
    return render(request,'website/edit.html',{'plant':plant})

def update(request,id):
	plant=new_Plant.objects.get(id=id)
	form=PlantForm(request.POST,instance=plant)
	if form.is_valid():
		form.save()
		return redirect("/show")
	return render('edit.html ',{'plant':plant})

def destroy(request,id):
    plant=new_Plant.objects.get(id=id)
    plant.delete()
    return redirect("/show")


#Gateway views : 

def Gateway(request):
	if request.method=="POST":
		form=GatewayForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/showgateway')
			except:
				pass
	else:
		form=GatewayForm()
	return render(request,'website/indexgateway.html',{'form':form})

def show_Gateway(request):
    gateways=new_Gateway.objects.all()
    return render(request,'website/showgateway.html',{'gateways':gateways})		

def edit_Gateway(request,id):
    gateway=new_Gateway.objects.get(id=id)
    return render(request,'website/editgateway.html',{'gateway':gateway})

def update_Gateway(request,id):
	gateway=new_Gateway.objects.get(id=id)
	form=GatewayForm(request.POST,instance=gateway)
	if form.is_valid():
		form.save()
		return redirect("/showgateway")
	return render(request,'website/editgateway.html ',{'gateway':gateway})

def destroy_Gateway(request,id):
    gateway=new_Gateway.objects.get(id=id)
    gateway.delete()
    return redirect("/showgateway")

#Devices views : 



def device(request):
	if request.method=="POST":
		form=DeviceForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/showdevice')
			except:
				pass
	else:
		form=DeviceForm()
	return render(request,'website/indexdevice.html',{'form':form})

def show_Device(request):
    devices=new_Device.objects.all()
    return render(request,'website/showdevice.html',{'devices':devices})		

def edit_Device(request,id):
    device=new_Device.objects.get(id=id)
    return render(request,'website/editdevice.html',{'device':device})

def update_Device(request,id):
	device=new_Device.objects.get(id=id)
	form=DeviceForm(request.POST,instance=device)
	if form.is_valid():
		form.save()
		return redirect("/showdevice")
	return render(request,'website/editdevice.html',{'device':device})

def destroy_Device(request,id):
    device=new_Device.objects.get(id=id)
    device.delete()
    return redirect("/showdevice")

# Rendering gateway's device

def gatewaysdevice(request,id):
    gateway=new_Gateway.objects.get(id=id)
    result=new_Device.objects.filter(Gateway_Name__contains=gateway.gatewayname)
    return render(request, 'website/gatewaysdevice.html',{'result':result})


# Rendering plant data as json :
def plant_json(request):
    data=list(new_Plant.objects.values())
    return JsonResponse(data,safe=False)
# Rendering Gateway data as json :
def gateway_json(request):
    data=list(new_Gateway.objects.values())
    return JsonResponse(data,safe=False)
# Rendering Device data as json :
def device_json(request):
    data=list(new_Device.objects.values())
    return JsonResponse(data,safe=False)

    
        





    
               


	




