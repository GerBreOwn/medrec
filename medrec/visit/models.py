#from sqlalchemy import Column, Integer, String
#from sqlalchemy.types import DateTime
from django.db import models
from django.db import connection
from django.db.models import F
from django.db.models import signals
from django.contrib.auth.models import User
from django.utils import timezone
from django.apps import AppConfig
import datetime
from crum import get_current_user
from django.contrib import admin
from patient.models import Patient

class CommonInfo(models.Model): #1
	is_active = models.BooleanField(default = True, editable = False)
	created_on = models.DateTimeField(auto_now_add = True, editable = False)
	created_by = models.ForeignKey('auth.User', blank=True, null=True, editable = False, default = None, related_name = "+")
	modified_on = models.DateTimeField(auto_now = True)
	modified_by = models.ForeignKey('auth.User', blank = True, null = True, default = None, editable = False)
	counter = models.IntegerField(blank = True, null = True, default = None, editable = False)

	def get_model_perms(self, *args, **kwargs):
		perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
		perms['list_hide'] = True
		return perms

	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.created_by = user
		self.modified_by = user

		super(CommonInfo, self).save(*args, **kwargs)

	def count_changes(self):
		with connection.cursor() as cursor:
			cursor.execute("update self set counter =+ 1 where self.id = %s", [self.pk])


	class Meta:
		#ordering = ['-counter',]
		abstract = True


class Biopsy(CommonInfo): #2
	id = models.AutoField(primary_key=True)
	biopsy_name = models.ForeignKey('BiopsyName',blank = True, null = True)
	biopsy_location = models.ForeignKey('Location', blank = True, null = True)
	biopsy_result = models.ForeignKey('BiopsyResult', blank = True, null = True)
	biopsy_text = models.TextField(blank = True, null = True)
	visit = models.ForeignKey('Visit', blank = True, null = True, editable = False)

	def get_absolute_url(self):
		return reverse('biopsy-detail', args=[str(self.id)])

	class meta:
		app_label = 'Biopsy'
		#ordering = [ 'biopsy_name', '-counter']

	def __str__(self):
		return '%s' % (self.biopsy_name)

class BiopsyName(CommonInfo):
	id = models.AutoField(primary_key=True)
	biopsy_name = models.CharField(max_length=25, blank = False, null = False, unique = True)

	class meta:
		app_label = 'BiopsyName'
		ordering = ['-counter', 'biopsy_name']
		verbose_name = "biopsies"

	def get_absolute_url(self):
		return reverse('biopsy-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.biopsy_name)


class BiopsyResult(CommonInfo): #3
	id = models.AutoField(primary_key=True)
	biopsy_result = models.CharField(max_length=25, blank = False, null = False)

	class Meta:
		ordering = ['-counter','biopsy_result']

	def get_absolute_url(self):
		return reverse('biopsyresult-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.biopsy_result)

class ComplaintName(CommonInfo):
	id = models.AutoField(primary_key=True)
	complaint_name = models.CharField(max_length=255, unique = True, blank=False, null=False)
	#visit = models.ForeignKey('Visit', blank = True, null = True, editable = False)

	def __str__(self):
		return '%s' % (self.complaint_name)

	class meta:
		ordering = ["complaint_name",]

	def get_absolute_url(self):
		return reverse('complaintname-detail', args=[str(self.id)])

class Complaint(CommonInfo): #4
	id = models.AutoField(primary_key=True)
	complaint_name = models.ForeignKey(ComplaintName, blank = False, null = False)
	complaint_location = models.ForeignKey('Location', blank = False, null = False)
	visit = models.ForeignKey('Visit', blank = True, null = True, editable = False)
	finding = models.ManyToManyField('Finding')
	treatment = models.ManyToManyField('Treatment')

	def get_absolute_url(self):
		return reverse('complaint-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.complaint_name)

	class meta:
		ordering = ['-counter', 'complaint_name',]

class Dose(CommonInfo): #5
	id = models.AutoField(primary_key=True)
	dose_name = models.CharField(max_length=25, unique = True)

	class Meta:
		ordering = ['-counter', 'dose_name']

	def get_absolute_url(self):
		return reverse('dose-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.dose_name)

#class Drawing(CommonInfo): #6
	#id = models.AutoField(primary_key=True)
	#patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
	#drawing_name = models.BinaryField(blank=True, null=True, unique = True)

	##class Meta:
		##ordering = ['-counter', 'patient', 'drawing_name']

	#def get_absolute_url(self):
		#return reverse('drawing-detail', args=[str(self.id)])

	#def __str__(self):
		#return '%s, %s' % (self.dra_name, self.patient)

class ExamName(CommonInfo):
	id = models.AutoField(primary_key = True)
	exam_name = models.CharField(max_length = 25, blank = True, null = True, unique = True)
	visit = models.ForeignKey('Visit', blank = True, null = True, editable = False)

class Exam(CommonInfo): #7
	id = models.AutoField(primary_key = True)
	exam_name = models.ForeignKey(ExamName, blank = True, null = True)
	exam_date = models.DateField(blank=True, null=True)
	exam_type = models.ForeignKey('ExamType', blank=True, null=True)
	exam_result = models.ForeignKey('ExamResult', blank=True, null=True)
	exam_text = models.TextField(blank=True, null=True)
	visit = models.ForeignKey('Visit', blank = True, null = True, editable = False)

	def get_absolute_url(self):
		return reverse('exam-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.exam_date, self.exam_name)

class ExamResult(CommonInfo): #8
	id = models.AutoField(primary_key=True)
	exam_result = models.CharField(max_length=25, blank=True, null=True, unique = True)

	def get_absolute_url(self):
		return reverse('examresult-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.exam_result)

class ExamType(CommonInfo): #9
	id = models.AutoField(primary_key=True)
	exam_type = models.CharField(max_length=25, blank=True, null=True, unique = True)

	def get_absolute_url(self):
		return reverse('examtype-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.exam_type)

class Finding(CommonInfo): #10
	id = models.AutoField(primary_key=True)
	finding_name = models.CharField(max_length=255, blank = True, null = True)#, unique = True)
	visit = models.ForeignKey('Visit', blank = True, null = True, editable = False)

	class Meta:
		ordering = ['-counter', 'finding_name']

	def get_absolute_url(self):
		return reverse('finding-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.finding_name)

class Hearing(CommonInfo):
	id = models.AutoField(primary_key=True)
	hearing_test = models.ForeignKey('HearingTest', blank = True, null = True)
	hearing_result = models.ForeignKey('HearingResult', blank = True, null = True)
	hearing_text = models.TextField(blank=True, null=True)
	visit = models.ForeignKey('Visit', blank = True, null = True, editable = False)

class HearingTest(CommonInfo): #11
	id = models.AutoField(primary_key=True)
	hearing_name = models.CharField(max_length = 50, blank=True, null = True, unique = True)

	class Meta:
		ordering = ['-counter', 'hearing_name']

	def get_absolute_url(self):
		return reverse('hearing-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.hearing_name)

class HearingResult(CommonInfo): #12
	id = models.AutoField(primary_key=True)
	hearing_result = models.CharField(max_length=25, unique = True)

	class Meta:
		ordering = ['-counter', 'hearing_result']

	def __str__(self):
		return '%s' % (self.hearing_result)

class Location(CommonInfo): #13
	id = models.AutoField(primary_key = True)
	location = models.CharField(max_length = 25,blank=False, null=False, unique = True)

	class Meta:
		ordering = ['-counter', 'location']

	def get_absolute_url(self):
		return reverse('location-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.location)

class Medicine(CommonInfo): #14
	id = models.AutoField(primary_key=True)
	brand_name = models.CharField(max_length=50, blank = True, null = True, unique=True)
	generic_name = models.CharField(max_length = 50, blank = True, null = True)

	class Meta:
		ordering = ['-counter', 'brand_name']

	def get_absolute_url(self):
		return reverse('medication-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.brand_name)


class Prescription(CommonInfo):
	id = models.AutoField(primary_key=True)
	patient = models.ForeignKey(Patient, blank=True, null=True)#, editable = False)
	medicine = models.ForeignKey(Medicine, blank=True, null=True)
	medicine_dose = models.ForeignKey(Dose, blank=True, null=True)
	prescription_reminder = models.ForeignKey('Reminder', blank=True, null=True)
	medicine_quantity = models.IntegerField(blank=True, null=True)
	visit = models.ForeignKey('Visit', blank = True, null = True, editable = False)
	PPRINT = (('Y', 'Yes'), ('N', 'No'),)
	pprint = models.CharField(max_length=1, choices=PPRINT, blank=False, null=False, default = 'Y', help_text = 'Print this prescription?')

	PRE_PAPER = (('P', 'Plain Paper'), ('H', 'With Headers'),)
	pre_paper = models.CharField(max_length=1, choices=PRE_PAPER, blank=True, null=True, help_text = 'Select paper type.')

	def get_absolute_url(self):
		return reverse('prescription-detail', args=[str(self.id)])

	#def __str__(self):
		#return '%s' % (self.medicine)

class Reminder(CommonInfo):
	id = models.AutoField(primary_key=True)
	prescription_reminder = models.CharField(max_length=50, blank = True, null = True, unique = True)

	class Meta:
		ordering = ['-counter', 'prescription_reminder']

	def get_absolute_url(self):
		return reverse('reminder-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.prescription_reminder)


class Treatment(CommonInfo):
	id = models.AutoField(primary_key=True)
	treatment_name = models.CharField(max_length=255, blank = True, null = True)
	visit = models.ForeignKey('Visit', blank = True, null = True, editable = False)

	class Meta:
		ordering = ['-counter', 'treatment_name']

	def get_absolute_url(self):
		return reverse('treatment-detail', args=[str(self.id)])

	def __str__(self):
		return '%s' % (self.treatment_name)

class Visit(CommonInfo): #22
	id = models.AutoField(primary_key=True)
	visit_date = models.DateField(blank=False, null=False)
	patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=False, null=False)

	def get_absolute_url(self):
		return reverse('visit-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.patient, self.visit_date)
