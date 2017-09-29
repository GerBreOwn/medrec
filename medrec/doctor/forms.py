#import floppyforms as fforms

class PrescriptionForm(fforms.Form):
	dr_name = fforms.CharField()
	dr_suffix = fforms.CharField()
	dr_phone = fforms.CharField()

