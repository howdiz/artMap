from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list, object_detail
from artmaps.maps.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


show_dict = {
	'queryset': Show.objects.select_related().all().order_by('-opening_date'),
	#'template_name': 'maps/show_list.html',
	"extra_context" : {"location_list" : Location.objects.select_related().all()}
}

show_detail_dict = dict(show_dict, **{
	'id': 'id',
	'template_name': 'maps/show_detail.html',
})



urlpatterns = patterns('',
    # Example:
    # (r'^artmaps/', include('artmaps.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^listings/$', 'artmaps.maps.views.index'),
    
   # (r'^$', 'django.views.generic.list_detail.object_list', show_dict),
    
    (r'^$', 'artmaps.maps.views.index'), 
	
    (r'^show_json/$', 'artmaps.maps.views.show_json'),

    (r'^event_json/$', 'artmaps.maps.views.event_json'),
	
	(r'^picks_json/$', 'artmaps.maps.views.picks_json'),

    (r'^gallery_json/$', 'artmaps.maps.views.gallery_json'),

    (r'^location_json/$', 'artmaps.maps.views.location_json'),
    
    #(r'^listings/?P<show_id>\d+)/$', 'artmaps.maps.views.detail'),
    
    (r'^admin/', include(admin.site.urls)),

    #(r'^$', direct_to_template, {'template': 'maps/index.html'}),    

    #(r'^listings/$', object_list, show_dict ),

    #(r'^listings/(?P<id>[-\w]+)/$', object_detail, show_detail_dict),	
)
