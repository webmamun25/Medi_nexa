from django.db import models
from patient.models import Patient
from doctor.models import Doctor,Availabletime
# Create your models here.
APPOINTMENT_TYPES=[
    ('Online','Online'),
    ('Offline','Offline')
    
]
APPOINTMENT_STATUS=[
    ('Pending','Pending'),
    ('Running','Running'),
    ('Completed','Completed'),
    
]
class Appointment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    availabletime=models.ForeignKey(Availabletime,on_delete=models.CASCADE)
    appointment_type=models.CharField(choices=APPOINTMENT_TYPES,max_length=224)
    appointment_status=models.CharField(choices=APPOINTMENT_STATUS,max_length=224,default="Pending")
    symptoms=models.TextField()
    cancel=models.BooleanField(default=False)