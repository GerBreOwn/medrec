from django.db import models
from crum import get_current_user
from django.contrib import admin

class CommonInfo(models.Model):
    is_active = models.BooleanField(default = True, editable = False)
    created_on = models.DateTimeField(auto_now_add = True, editable = False)
    created_by = models.ForeignKey('auth.User', blank=True, null=True, editable = False, default = None, related_name = "+", on_delete=models.SET_DEFAULT)
    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey('auth.User', blank = True, null = True, default = None, editable = False, on_delete=models.SET_DEFAULT)
    counter = models.IntegerField(blank = True, null = True, default = None, editable = False)

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
        ordering = ['-counter',]
        abstract = True

class Doctor(CommonInfo):
    id = models.AutoField(primary_key = True)
    dr_name = models.CharField(max_length = 55)
    dr_suffix = models.CharField(max_length = 55, blank = True, null = True)
    dr_telephone = models.CharField(max_length = 12, blank = True, null = True)
    dr_affil1 = models.ManyToManyField('Hospital',max_length = 25)#, blank = True, null = True)
    dr_ptr_no = models.CharField(max_length = 25, blank = True, null = True)
    dr_s2_no = models.CharField(max_length = 25, blank = True, null = True)

    def get_absolute_url(self):
        return reverse('doctor-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.dr_name)

class Hospital(CommonInfo):
    id = models.AutoField(primary_key = True)
    hosp_name = models.CharField(max_length = 25, blank = True, null = True)

    def get_absolute_url(self):
        return reverse('hospital_affiliat-detail', args=[str(self.id)])

    def __str__(self):
        return '%s' % (self.hosp_name)


#class Office_Hours(CommonInfo):
    #id = models.AutoField(primary_key = True)
    #days = models.CharField(max_length = 20, blank = True, null = True)
    #hours_am = models.CharField(max_length = 20, blank = True, null = True)
    #hours_pm = models.CharField(max_length = 20, blank = True, null = True)
    #doctor = models.ForeignKey('Doctor')

    #def get_absolute_url(self):
        #return reverse('office_hours-detail', args=[str(self.id)])

    #def __str__(self):
        #return '%s %s' % (self.days, self.hours)

