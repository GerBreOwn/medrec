from django.contrib import admin

# Register your models here.

from .models import Doctor

mymodels = [Doctor]

admin.site.register(mymodels)

class DoctorAdmin(admin.ModelAdmin):
	view_on_site = False
