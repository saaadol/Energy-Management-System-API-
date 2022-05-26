
from django.db import models


# This is the Choices  :
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
infos_VFD= (
    ('VFD','VFD'),
    ('MP','MP'),
    ('TP','TP'),
)


# This is USER DATA Model :

    
    
class User_Data(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    list_plant=models.CharField(max_length=100)
    
    
# This is Plant Model :
class Plant(models.Model):
    name=models.CharField(max_length=20)
    adress=models.CharField(max_length=50)
    type=models.CharField(max_length=20,choices=infos_type)
    location=models.CharField(max_length=50)
    list_gateway=models.CharField(max_length=50)
    status=models.CharField(max_length=50,choices=infos_status)
    
    def __str__(self):
        return self.name
    
# This is Gateway Model :
class Gateway(models.Model):
    gatewayname=models.CharField(max_length=20)
    serial_number=models.CharField(max_length=20)
    list_devices=models.CharField(max_length=20)
    def __str__(self):
        return self.gatewayname
       
    # This is Device Model : 
    
class Device(models.Model):
    Gateway_serialnumber=models.CharField(max_length=20)
    DeviceName=models.CharField(max_length=20)
    serial_number=models.CharField(max_length=20)
    adress=models.CharField(max_length=20)
    baud_rate=models.CharField(max_length=20)
    connection_type=models.CharField(max_length=20,choices=infos_Device)
    def __str__(self):
        return self.DeviceName  
    
     # This is VFD Model  
    
class VFD(models.Model):
    VFD_Type=models.CharField(max_length=20,choices=infos_VFD)
    VFD_Time= models.DateTimeField()
    VFD_Name=models.CharField(max_length=20)
    Serial_Number=models.CharField(max_length=20)
    Plant_Name=models.CharField(max_length=20)
    Gateway_Name=models.CharField(max_length=20)
    Adress=models.IntegerField()
    baud_rate=models.FloatField()
    c00=models.FloatField()
    c01=models.FloatField()
    c02=models.FloatField()
    c03=models.FloatField()
    c04=models.FloatField()
    c06=models.FloatField()
    c07=models.FloatField()
    c12=models.FloatField()
    c13=models.FloatField()
    c14=models.FloatField()
    c15=models.FloatField()
    c16=models.FloatField()
    c17=models.FloatField()
    c18=models.FloatField()
    c19=models.FloatField()
    c20=models.FloatField()
    c21=models.FloatField()
    c23=models.FloatField()
    c24=models.FloatField()
    c25=models.FloatField()
    c27=models.FloatField()
    
class Monophase (models.Model):
    Monophase_Type=models.CharField(max_length=20,choices=infos_VFD)
    Monophase_Time= models.DateTimeField()
    MonoPhase_Name=models.CharField(max_length=20)
    Serial_Number=models.CharField(max_length=20)
    Plant_Name=models.CharField(max_length=20)
    Gateway_Name=models.CharField(max_length=20)
    Adress=models.IntegerField()
    baud_rate=models.FloatField()
    Voltage=models.FloatField() 
    Current=models.FloatField()
    Active_Power= models.FloatField()
    Apparent_Power=models.FloatField()
    FP=models.FloatField()
    frenquency=models.FloatField()
    
class Triphase(models.Model):
    Triphase_Type=models.CharField(max_length=20,choices=infos_VFD)
    Triphase_Time= models.DateTimeField()
    Triphase_Name=models.CharField(max_length=20)
    Serial_Number=models.CharField(max_length=20)
    Plant_Name=models.CharField(max_length=20)
    Gateway_Name=models.CharField(max_length=20)
    Adress=models.IntegerField()
    Baud_Rate=models.FloatField()
    UA=models.FloatField()
    UB=models.FloatField()
    UC=models.FloatField()
    UAB=models.FloatField()
    UBC=models.FloatField()
    UAC=models.FloatField()
    IA=models.FloatField()
    IB=models.FloatField()
    IC=models.FloatField()
    frequency=models.FloatField()
    Pa=models.FloatField()
    Pb=models.FloatField()
    Pc=models.FloatField()
    Pt=models.FloatField()
    Qa=models.FloatField()
    Qb=models.FloatField()
    Qc=models.FloatField()
    Qt=models.FloatField()
    Sa=models.FloatField()
    Sb=models.FloatField()
    Sc=models.FloatField()
    St=models.FloatField()
    FPa=models.FloatField()
    FPb=models.FloatField()
    FPc=models.FloatField()
    FPt=models.FloatField()
    THDV=models.FloatField()
    THDI=models.FloatField()
    max_demand=models.FloatField()
    count_E=models.FloatField()
    count_Er=models.FloatField()
    
    
    
class test(models.Model):
    Voltage=models.FloatField() 
    Current=models.FloatField()
    Active_Power= models.FloatField()
    Apparent_Power=models.FloatField()
    FP=models.FloatField()
    frenquency=models.FloatField()
        
    
    
    
    
    
    
           
