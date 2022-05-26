from django.db import models
infos_type= (
    ('ONGRID','ONGRID'),
    ('PV','PV'),
    ('HYBRID','HYBRID'),
)
infos_status= (
    ('etude','Etude'),
    ('online','Online'),
    ('Other','Other'),
)
infos_Device= (
    ('Rs485','Rs485'),
    ('lora','lora'),
    ('Other','Other'),
)

class new_Plant(models.Model):
    name=models.CharField(max_length=20)
    adress=models.CharField(max_length=50)
    type=models.CharField(max_length=20,choices=infos_type)
    location=models.CharField(max_length=50)
    list_gateway=models.CharField(max_length=50)
    status=models.CharField(max_length=50,choices=infos_status)
    
    def __str__(self):
        return self.name    
    #class Meta:
        #db_table="website"
        
class new_Gateway(models.Model):
    gatewayname=models.CharField(max_length=20)
    slavename=models.CharField(max_length=20)
    list_devices=models.CharField(max_length=20)
    def __str__(self):
        return self.gatewayname
    
    
class new_Device(models.Model):
    Gateway_Name=models.CharField(max_length=20)
    DeviceName=models.CharField(max_length=20)
    slavename=models.CharField(max_length=20)
    adress=models.CharField(max_length=20)
    baud_rate=models.CharField(max_length=20)
    connection_type=models.CharField(max_length=20,choices=infos_Device)
    def __str__(self):
        return self.DeviceName
    

       
    
# Create your models here.
