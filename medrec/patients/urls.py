"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from sumedrec import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^admin_tools/', include('admin_tools.urls')),
	url(r'^patients/$', views.PatientListView.as_view(), name='patients'),
	url(r'^patients/(?P<pk>\d+)$', views.PatientDetailView.as_view(), name='patients-detail'),
	
	url(r'^visits/$', views.VisitListView.as_view(), name='visits'),  
    url(r'^visits/(?P<pk>\d+)$', views.VisitDetailView.as_view(), name='visits-detail'),
]

