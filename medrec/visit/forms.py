from django import forms
from django.forms import Widget
#import floppyforms as fforms

#class PrescriptionForm(fforms.Form):
	#dr_name = fforms.CharField()


class BiopsyForm(forms.ModelForm):
	class Meta:
		widgets = {
			#'biopsy': forms.Select(attrs = {'size': 20}),
			'biopsy_result': forms.Select(attrs = {'size': 30}),
		}

class ComplaintForm(forms.ModelForm):
	class Meta:
		widgets = {
			'complaintname': forms.Select(attrs = {'size': 30}),
			'location': forms.Select(attrs = {'size': 30}),
			'finding': forms.CheckboxSelectMultiple(attrs = {'size': 30}),
			'treatment': forms.CheckboxSelectMultiple(attrs = {'size': 30}),
		}

class ExamForm(forms.ModelForm):
	class Meta:
		widgets = {
			'exam': forms.Select(attrs = {'size': 30}),
			'exam_type': forms.Select(attrs = {'size': 30}),
			'exam_result': forms.Select(attrs = {'size': 30}),
			'exam_text': forms.TextInput(attrs = {'size': 30}),
		}

class HearingForm(forms.ModelForm):
	class Meta:
		widgets = {
			'hearing_test': forms.Select(attrs = {'size': 30}),
			'hearing_result': forms.Select(attrs = {'size': 30}),
			'hearing_text': forms.TextInput(attrs = {'size': 30}),
		}

class PrescriptionForm(forms.ModelForm):
	class Meta:
		widgets = {
			'medicine': forms.Select(attrs = {'size': 30}),
			'medicine_dose': forms.Select(attrs = {'size': 30}),
			'medicine_quantity': forms.TextInput(attrs = {'size': 10}),
			'reminder': forms.TextInput(attrs = {'size': 30}),
		}
