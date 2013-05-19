var markers;
jQuery.noConflict();
jQuery(document).ready(function($){
  $("#login-toggle").click(function() {
    $('.login-container').slideToggle(300,function(){
      $("#login-toggle").text('LOG IN').stop();
    });
    $('.signup-container').slideToggle(300, function(){
       $("#login-toggle").text('sign up now').stop();
    });
  });

  markers = new L.MarkerClusterGroup();
  load_people("/api/geoperson", "");

});

function load_people(filters, url) {
  var people = jQuery.getJSON((url + filters), function(data) {
    console.log( "success" );
      jQuery.each(data.objects, function (key, val) {
        lng = val.location.coordinates[0];
        console.log(lng);
        lat = val.location.coordinates[1];
        console.log(lat);
        name = val.name;
        var marker = new L.marker([lat, lng]);
        // var marker = L.circleMarker([lat, lng], 200)
        marker.bindPopup(name);
        markers.addLayer(marker);
      });
    map.addLayer(markers); 
  })
  .done(function(data) {
    console.log( "second success" ); 
    var next = data.meta.next;
    console.log(next);
    if (next !== null) {
      load_people(next, "");
    }
  })
  .fail(function() { console.log( "error" ); })
  .always(function() { console.log( "complete" ); });
};
