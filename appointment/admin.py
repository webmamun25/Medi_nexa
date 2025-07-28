from django.contrib import admin
from django.template.loader import render_to_string
# Register your models here.
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
class AppAdmin(admin.ModelAdmin):
    list_display=('patient__user__first_name','doctor__user__first_name','appointment_type','appointment_status','symptoms','cancel')


    def save_model(self, request, obj, form, change):
        obj.save()
        if(obj.appointment_type=='Online' and obj.appointment_status=='Running'):
            subject = "check your appointment"
            email_body=render_to_string('admin_email.html',{'user':obj.patient.user,'doctor':obj.doctor})
            msg = EmailMultiAlternatives(subject,'', to=[obj.patient.user.email])
            msg.attach_alternative(email_body, "text/html")
            msg.send()
admin.site.register(Appointment,AppAdmin)