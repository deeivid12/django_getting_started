from django.shortcuts import render, get_object_or_404
from django.forms import modelform_factory
from meetings.models import Meeting, Room

MeetingForm = modelform_factory(Meeting, exclude=[])

def detail(request, id):
	meeting = get_object_or_404(Meeting, pk=id)
	data = {"meeting": meeting}
	return render(request, "meetings/detail.html", data)

def all_rooms(request):
	rooms = Room.objects.all()
	data = {"rooms": rooms}
	return render(request, "rooms/rooms.html", data)

def new(request):
	form = MeetingForm()
	data = {"form": form}
	return render(request, "meetings/new.html", data)
