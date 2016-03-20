

$(document).ready(function(){
  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;

      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide");
        }
    });
  });
  
});

var map;
var marker;

function initMap() {
	
	// init map - with some location..
	var myLatLng = {lat: -34.397, lng: 150.644};
	map = new google.maps.Map(document.getElementById('map'), {
	    center: myLatLng,
	    disableDoubleClickZoom: true,
	    zoom: 8
	});
	
	// create one marker
	marker = new google.maps.Marker({
	    position: myLatLng,
	    draggable: true,
	    animation: google.maps.Animation.DROP,
	    map: map
	});
	

	// on dbl-click - put the marker there	
	google.maps.event.addListener(map, 'dblclick', function(event) {
	    marker.setPosition(event.latLng, map);
	    // update place text box
	    $(search_input).val("").attr("placeholder", "(Custom location)");
	});

	// init place input - assuming id='id_place'
	var search_input = document.getElementById("id_place");
	$(search_input).attr("placeholder", "Search for address or place");
	
	// set the place input to implement autocomplete and bind to the map
	var autocomplete = new google.maps.places.Autocomplete(search_input, {types: ['geocode']});
	autocomplete.bindTo('bounds', map);
	
	// what to do when a place is changed (by the 'place' input)
	google.maps.event.addListener(autocomplete, 'place_changed', function() {
		var place = autocomplete.getPlace();
		// If the place has a geometry, then present it on a map.
	    if (place.geometry.viewport) {
	      	map.fitBounds(place.geometry.viewport);
	    } else {
	      	map.setCenter(place.geometry.location);
	      	map.setZoom(17);  // Why 17? Because it looks good.
	    }
	    
	    marker.setPosition(place.geometry.location);
	    
	    $(search_input).attr("placeholder", "Search for address or place");
	});
	  
}


function initRadius(){
	radius_input = $("#id_distance");
	
	// Add circle overlay and bind to marker
	var circle = new google.maps.Circle({
		  map: map,
		  radius: $(radius_input).val(),    
		  strokeColor: '#FF0000',
	      strokeOpacity: 0.8,
	      strokeWeight: 1,
	      fillColor: '#FF0000',
	      fillOpacity: 0.35,
	});
	circle.bindTo('center', marker, 'position');
	

	$( "#slider" ).slider({
      min: 10,
      max: 200000,
      value: $(radius_input).val(),
      slide: function( event, ui ) {
        circle.setRadius( ui.value );
        
    	updating = true;
    	$(radius_input).val(ui.value);
    	updating = false;
      } ,
      change: function( event, ui ) {
		circle.setRadius( ui.value );
      }
	});
	
    $(radius_input).change(function(){
    	if (!updating){
    		$( "#slider" ).slider("value", $(this).val());
    	}
    });
    
    circle.setRadius( $( "#slider" ).slider("value") );
}
