from django.http import HttpResponse

def index(request_uri):
	return HttpResponse("Welcome to the Medical Records (medrec) program.")
