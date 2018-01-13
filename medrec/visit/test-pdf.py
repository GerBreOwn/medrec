from reportlab.lib.pagesizes import HALF_LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Image, Paragraph, Table
from datetime import date
from django.db import models
from django.db import connection
from models import Patient, Visit

def __init__(self, connection):
        self.connection = connection

patient = Patient.objects.all(
''''SELECT 
  patient_patient.patient_last_name::text || ', ' || patient_patient.patient_first_name::text as fullname, 
  extract(year from age(patient_patient.patient_date_of_birth)) AS age, 
  patient_patient.patient_gender, 
  visit_medicine.brand_name, 
  visit_medicine.generic_name, 
  visit_dose.dose_name, 
  visit_prescription.medicine_quantity, 
  visit_reminder.prescription_reminder
FROM 
  public.visit_visit, 
  public.patient_patient, 
  public.visit_prescription, 
  public.visit_medicine, 
  public.visit_dose, 
  public.visit_reminder
WHERE 
  visit_visit.patient_id = patient_patient.id AND
  visit_prescription.visit_id = visit_visit.id AND
  visit_prescription.medicine_id = visit_medicine.id AND
  visit_prescription.medicine_dose_id = visit_dose.id AND
  visit_prescription.prescription_reminder_id = visit_reminder.id AND
  visit_visit.id = 6;''')

        
fullname = "Brown, Gerald S"
age = "74"
sex = "M"
address = "Dumaguete City"

dt = date.today()

c = canvas.Canvas("testform.pdf", pagesize=HALF_LETTER)
c.setLineWidth(.3)
c.setFont('Helvetica-Bold', 14)

c.setPageSize((396,612))

c.drawString(40, 576, 'SIMON JOHN ERIC T. FLORES, M.D., DPBO-HNS')

c.setFont('Helvetica-Bold', 11)
c.drawString(60,556, 'Diplomate - Ears, Nose, Throat - Head and Neck Surgery')

c.drawString(36,526,'SUMC')
c.setFont('Helvetica-Bold', 9)
c.drawString(36,516,'Mon. - Fri.:   10:00 A.M. - 12:00 NN')
c.drawString(36,506,'                      2:00 P.M. -  4:00 P.M.')
c.drawString(36,496, 'Saturday  :   10:00 A.M. - 12:00 NN')
c.drawString(36,486, 'Tel. No.    :   420-2217')

c.setFont('Helvetica-Bold', 10)
c.drawString(265,506,'HOSPITAL AFFILIATIONS:')
c.drawString(265,496,'NOPH')
c.drawString(265,486,'Holy Child Hospital')

c.line(35,463,378,479)
c.line(35,461,378,477)

c.setFont('Helvetica-Bold', 10)
c.drawString(36,456,'Patient')
c.drawString(74,458,'%s' % fullname)
c.drawString(270,456,'Age')
c.drawString(292,458,'%s' % age)
c.drawString(330,456,'Sex')
c.drawString(352,458,'%s' % sex)

c.drawString(36, 436, 'Address')
c.drawString(77, 438, '%s' %  address )
c.drawString(270, 436, 'Date')
c.drawString(303, 438, '%s' % dt)

c.line(72,456,266,456)
c.line(290,456,325,456)
c.line(350,456,378,456)
c.line(72,436,266,436)
c.line(300,436,378,436)

# But first to put in the logo
logo = Image("images.png")
logo.drawHeight = 1*inch
logo.drawWidth = 1*inch
#c.logo.wrap((c,72, 72))
#c.logo.drawOn(36,390)
#c.drawImage(logo, 360,390)

# Now to enter some medicines!!!
pres1 = "Medicine1  20mg  #30 "
c.drawString(72, 396, "%s" % pres1)

# Below is the code for the footer.
c.line(252,54,342,54)
c.drawString(344,55,'M.D.')
c.drawString(252, 43, 'Lic.No.: 0092579')
c.drawString(252, 31, 'PTR No.:')
c.line(292, 31, 360,31)
c.drawString(252,19, 'S2 No.:')
c.line(288, 19,360,19)

c.save()
