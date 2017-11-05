from django.http import HttpResponse

def index(request_uri):
	return HttpResponse("Welcome to the Medical Records (medrec) program.")

def about(request):
	return HttpResponse("This is the about page for the Medical Records (medrec) program")
