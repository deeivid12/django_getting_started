from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from meetings.models import Meeting

# Create your views here.

def welcome(request):
	data = {"day": date.today(), "num_meetings": Meeting.objects.count(),
        	"meetings": Meeting.objects.all()}
	return render(request, "website/welcome.html", data)

def about_me(request):
	return HttpResponse("About me")
