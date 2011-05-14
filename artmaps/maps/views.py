from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from artmaps.maps.models import Show, Gallery, Location, Event
from datetime import datetime
from itertools import chain

def index(request):
	today=datetime.now().date()
	this_month_shows = Show.objects.filter(opening_date__month=today.month)
	this_month_shows = this_month_shows.filter(end_date__gte=today)
	ongoing_shows  = Show.objects.exclude(opening_date__month=today.month)
	ongoing_shows = ongoing_shows.filter(end_date__gte=today)
	shows = this_month_shows | ongoing_shows
	events = Event.objects.filter(date__gte=datetime.now().date()).order_by('date')
	event_types = events.values_list('event_type', flat=True).distinct()
	return render_to_response('maps/index.html', {
		'shows': shows,
		'ongoing_shows': ongoing_shows,
		'this_month_shows': this_month_shows,
		'events': events,
		'event_types': event_types,
		'today': today
	})

def show_json(request):
	shows = Show.objects.filter(end_date__gte=datetime.now().date()).order_by('-opening_date')	
	json_data = serializers.serialize("json", shows, relations={'gallery':{'relations':('location')}})
	return HttpResponse(json_data, mimetype="application/json")

def event_json(request):
	events = Event.objects.filter(date__gte=datetime.now().date()).order_by('date')
	json_data = serializers.serialize("json", events, relations={'gallery':{'relations':('location')}})
	return HttpResponse(json_data, mimetype="application/json")

def picks_json(request):
	shows = Show.objects.filter(end_date__gte=datetime.now().date()).order_by('-opening_date').filter(pick__exact=True)	
	show_json = serializers.serialize("json", shows, relations={'gallery':{'relations':('location')}})
	events = Event.objects.filter(date__gte=datetime.now().date()).order_by('date').filter(pick__exact=True);
	event_json = serializers.serialize("json", events, relations={'gallery':{'relations':('location')}})	
	json_data = show_json | event_json
	return HttpResponse(json_data, mimetype="application/json")

def gallery_json(request):
	gallery_objects = list(Gallery.objects.all())
	json_data = serializers.serialize("json", gallery_objects)
	return HttpResponse(json_data, mimetype="application/json")

def location_json(request):
	location_objects = list(Location.objects.all()) + list(Show.objects.all().order_by('-opening_date')) + list(Gallery.objects.all())
	json_data = serializers.serialize("json", location_objects)
	return HttpResponse(json_data, mimetype="application/json")

#def detial(request, show_id):
#    s = get_objet_or_404(Show, pk=show_id)
#    return render_to_response('listings/detial.html', {'shows': shows})
	

