from django.contrib import admin
from django.core.urlresolvers import reverse

admin.site.site_title = 'Medical Records Administration'
admin.site.site_header = 'Medical Records Administration'

# Register your models here.

from .models import  Biopsy, BiopsyResult, Dose, ExamResult, ExamType,  Exam, HearingTest, HearingResult, Visit, Finding, Treatment, Prescription, Location, ComplaintName, BiopsyName, Hearing, ExamName, Reminder, Medicine, Complaint, Patient

mymodels = [BiopsyResult, Dose, ExamResult, ExamType, HearingTest, HearingResult, Treatment, Location, ComplaintName, BiopsyName, Hearing, ExamName, Reminder, Medicine, Finding]

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

#from .forms import BiopsyForm, ComplaintForm, ExamForm

#class HiddenModelAdmin(admin.ModelAdmin):
    #def get_model_perms(self, *args, **kwargs):
        #perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
        #perms['list_hide'] = True
        #return perms

class BiopsyAdminInline(admin.TabularInline):
	model = Biopsy
	classes = ['collapse']
	extra = 1

class ComplaintAdminInline(admin.TabularInline):
	model = Complaint
	extra = 1

class ExamAdminInline(admin.TabularInline):
	model = Exam
	classes = ['collapse']
	extra = 1

#class FindingAdminInline(admin.TabularInline):
	#model = Finding
	#extra = 1

class HearingAdminInline(admin.TabularInline):
	model = Hearing
	classes = ['collapse']
	extra = 1

class PrescriptionAdminInline(admin.TabularInline):
	model = Prescription
	extra = 1


@admin.register(Visit)
class VisitInstanceAdmin(admin.ModelAdmin):
	view_on_site = False
	fieldsets = (
	('Date & Patient:', {
	'fields': [('visit_date', 'patient')]
	}),
	)
	view_on_site = False

	inlines = (ComplaintAdminInline, PrescriptionAdminInline, BiopsyAdminInline, HearingAdminInline, ExamAdminInline, )

