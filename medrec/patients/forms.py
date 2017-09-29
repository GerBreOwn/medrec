from django import forms
from django.forms import Widget

class PatientForm(forms.ModelForm):
	class Meta:
		widgets = {
			'last_name': forms.TextInput(attrs = {'size': 25}),
			'first_name': forms.TextInput(attrs = {'size': 25}),
			'middle_initial': forms.TextInput(attrs = {'size': 1}),
			'address': forms.TextInput(attrs = {'size': 25}),
			'town': forms.TextInput(attrs = {'size': 25}),
			'date_of_birth': forms.TextInput(attrs = {'size': 25}),
			'email': forms.TextInput(attrs = {'size': 25}),
			'occupation': forms.TextInput(attrs = {'size': 25}),
		}
