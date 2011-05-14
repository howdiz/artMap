var shows, events;
$(function() {
	$("#tabs").tabs().addClass('ui-tabs-vertical ui-helper-clearfix');
	$("#tabs li").removeClass('ui-corner-top').addClass('ui-corner-left');
	//$("#check").button();
	//$("#format").buttonset();
	$("#cali").click(function() {
		$("#calilist").show();
	});
	$("#go").click(function() {
		$("#calilist").hide();
	});

	$("input[name=openings]").click(function() {
		mapStuff(shows);
	});
	
	$("input[name=closings]").click(function() {
		mapStuff(shows);
	});	
	
	$(".go").click(function() {
		mapStuff(shows);
	});

	$("input[name=event_type]").click(function() {
		mapEvents()
	});

	$('#tabs').bind('tabsselect', function(event, ui) {
		delegateThatTab(ui);	
	});
		
	$.getJSON("show_json",
    	function(data){
			shows = data;
			mapStuff(shows);
	});
});	

function delegateThatTab(tab) {	
	switch(tab.index) {
		case 0:
			mapStuff(shows);
			break;
		case 1:
			mapEvents();
			break;
		case 2:
			mapPicks();
			break;
	}
}
function mapPicks() {
	if(events === undefined) {
		$.getJSON("event_json",
			function(data) {
				events = data;
				//addLocationMarkers();
		});
	}
	
	var locations = new Array();
	for(i=0; i<shows.length; i++) { 
		if(shows[i].fields.pick===true) {
			addLocation(locations, shows[i]);
		}
	}
	for(i in events) {
		if(events[i].fields.pick===true) {
			addLocation(locations, events[i]);
		}
	}
	setMarkers(locations);	
}


function mapEvents() {
	if(events === undefined) {
		$.getJSON("event_json",
			function(data) {
				events = data;
				addLocationMarkers();
		});
	} else {
		addLocationMarkers();
	}
	function addLocationMarkers() {
		var locations = new Array();
		types = new Array();
		
		$types = $("input[name=event_type]:checked");
		
		for(key in events) {
			$types.each( function(i) {
				if(events[key].fields.event_type ===  $(this).val()){
					addLocation(locations, events[key]);
				}
			});	
		}		
		console.log(locations);
		setMarkers(locations);
	}
}

function mapStuff(shows) {
	var locations = new Array();
	for(i=0; i<shows.length; i++) { 
		if(filterShow(shows[i])) {
			addLocation(locations, shows[i]);
		}
	}
	setMarkers(locations);	
}

function addLocation(locations,thing) {
	locationId = thing.fields.gallery.fields.location.pk;
		
		if(locations[locationId]===undefined) 
			locations[locationId] = new Object();
		  	
	  	if(locations[locationId].info==undefined) {
		  	locations[locationId].info = "";
		}

		if(thing.model === 'maps.show') {		
			var bubbleInfo = $('#showBubbleTemplate').tmpl(thing);
		} else {
			var bubbleInfo = $('#eventBubbleTemplate').tmpl(thing);
		}
		locations[locationId].info += bubbleInfo.html();
		//locations[locationId].info += setInfo(thing);
		locations[locationId].address = thing.fields.gallery.fields.location.fields;
}

function filterShow(show) {

	var today = new Date();
	var nextWeek = new Date ();
	nextWeek.setDate(today.getDate() + 7);
		
	var endDate = new Date(show.fields.end_date);
	var startDate = new Date(show.fields.start_date);

	var showsIn;
	
	if($("input[name=openings]").is(":checked")) {
		if (startDate > today && startDate <= nextWeek) {
			showsIn =  true;
		} else {
			showsIn = false;
		}
	} else if($("input[name=closings]").is(":checked")) {
		if (endDate > today && endDate <= nextWeek) {
			showsIn =  true;
		} else {
			ShowsIn =  false;
		}
	} else { 
		showsIn =  true;
	}
	
	if(showsIn) {
		$("#show"+show.pk).show();
	} else {
		$("#show"+show.pk).hide();
	}
	return showsIn;
}

var map;


function setMarkers(locations) {
	var latlng = new google.maps.LatLng(39.952648,-75.163393);
    	var myOptions = {
      		zoom: 13,
      		center: latlng,
      		mapTypeId: google.maps.MapTypeId.ROADMAP,
			mapTypeControl: false,
			navigationControl: true,
			navigationControlOptions: {
				style: google.maps.NavigationControlStyle.ZOOM_PAN,
				position: google.maps.ControlPosition.RIGHT_CENTER
			},
			scaleControl: true,
			scaleControlOptions: {
				position: google.maps.ControlPosition.RIGHT_BOTTOM
			}
   		};
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    map.setCenter(latlng);
    
	var bubbleOpen = $("#bubbleOpen").html();
	var bubbleClose = $("#bubbleClose").html();
	
	for(i=0; i<locations.length; i++) {
		if(locations[i]!=undefined) {
		
        	latlng = new google.maps.LatLng(locations[i].address.latitude,locations[i].address.longitude);
        	
        	var marker = new google.maps.Marker({
            	map: map, 
            	position: latlng
        	});
			
			locations[i].info = bubbleOpen +  locations[i].info
			locations[i].info = locations[i].info + bubbleClose;			
        	 attachContent(marker, locations[i].info, i);
        	     	
    	}
  	}
  	
  	function attachContent(marker, infos, listingID) {
  	
	  	var onCLickFunction = function() {
			locId = i;
	  		infowindow.close();
	  		infowindow.setContent(infos);
			infowindow.open(map,marker);
			$(".sidebarListing").removeClass("ON");
			$('.location'+listingID).addClass("ON");
			$("#carousel").jcarousel({
        		scroll: 1,
    		});
		}
				
	  	$('.location'+listingID).live('click', onCLickFunction);
				
		google.maps.event.addListener(marker, 'click', onCLickFunction);
	
	}
}

function formatDate(datetime) {
	var dateObj = new Date(datetime);
	var dateStr = (dateObj.getMonth()+1) + "/" + dateObj.getDate() + "/" + dateObj.getFullYear();
	return dateStr;
}
