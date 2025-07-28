from django.contrib import admin
from .models import Specialization,Designation,Doctor,Availabletime,Ratings
# Register your models here.
class DesigAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("name",)}
class SpecialAdmin(admin.ModelAdmin):
    prepopulated_fields= {"slug": ("name",)}
    
admin.site.register(Designation,DesigAdmin)
admin.site.register(Specialization,SpecialAdmin)
admin.site.register(Doctor)
admin.site.register(Availabletime)
admin.site.register(Ratings)
