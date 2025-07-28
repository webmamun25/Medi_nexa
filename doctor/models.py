from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.

class Specialization(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=40)

    def __str__(self):
        return self.name 
    

class Designation(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=40)
    
    def __str__(self):
        return self.name 
    
class Availabletime(models.Model):
    time=models.CharField(max_length=30)
    
    def __str__(self):
        return self.time 

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='doctor/images')
    specialization=models.ManyToManyField(Specialization)
    designation=models.ManyToManyField(Designation)
    availabletime=models.ManyToManyField(Availabletime)
    fee=models.IntegerField()
    meet_link=models.TextField()
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
Rating_choices= [
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    ]

class Ratings(models.Model):
    reviewer=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    body=models.TextField()
    created_at=models.TimeField(auto_now_add=True)
    rating=models.CharField(choices=Rating_choices,max_length=40)
    
    class Meta:
       
        verbose_name_plural = 'Ratings'
    
    def __str__(self):
        return f"Patient {self.reviewer.user.first_name},Doctor {self.doctor.user.last_name}"