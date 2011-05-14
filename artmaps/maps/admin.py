from artmaps.maps.models import Location
from artmaps.maps.models import Gallery
from artmaps.maps.models import Show
from artmaps.maps.models import Event
from django.contrib import admin

class LocationAdmin(admin.ModelAdmin):
	list_display = ('nickname', 'address1', 'city', 'state', 'zipcode', 'url')

class ShowAdmin(admin.ModelAdmin):
	list_display = ('name', 'gallery', 'opening_date')
	list_filter = ['opening_date', 'gallery']
	search_fields = ['name', 'artist', 'description']
	fields = ['gallery','name', 'image', 'thumbnail', 'description', 
		  'start_date', 'end_date', 'opening_date', 'time_info',
		  'pick', 'artist']	

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'gallery', 'event_type', 'date')
	list_filter = ['date', 'gallery', 'event_type']
	search_fields = ['title', 'description']

admin.site.register(Location, LocationAdmin)
admin.site.register(Gallery)
admin.site.register(Show, ShowAdmin)
admin.site.register(Event, EventAdmin)
