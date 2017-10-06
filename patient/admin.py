from django.contrib import admin
from django.core.urlresolvers import reverse

admin.site.site_title = 'Medical Records Administration'
admin.site.site_header = 'Medical Records Administration'

# Register your models here.

from .models import  Patient, Province, Town, Occupation

mymodels = [Province, Town, Occupation]

def register_hidden_models(*model_names):
    for m in model_names:
        ma = type(
            str(m)+'Admin',
            (admin.ModelAdmin,),
            {
                'get_model_perms': lambda self, request: {}
            })
        admin.site.register(m, ma)

register_hidden_models(mymodels)

#admin.site.register(mymodels)

@admin.register(Patient)
class Patient(admin.ModelAdmin):
	view_on_site = False
	list_display = ('last_name', 'first_name', 'middle_initial', 'date_of_birth', 'contact_num', 'address', 'town','gender', 'email', 'occupation')
	fields = [('last_name', 'first_name', 'middle_initial'),('gender','date_of_birth'), ('contact_num', 'address', 'town'), ('email', 'occupation')]
	search_fields = ['last_name', 'first_name']

