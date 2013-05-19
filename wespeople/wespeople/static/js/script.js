var markers;
var people = [];

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
  if (from_year && to_year) {
    var url = "/api/geoperson?preferred_class_year__range=" + from_year + "," + to_year;
  } else if (from_year) {
    var url = "/api/geoperson?preferred_class_year=" + from_year;
  } else {
    var url = "/api/geoperson?preferred_class_year__gte=2010"
  }
  load_people(url, "");
  jQuery('#location-search').submit(function(e) {
      var s = $('#myForm :input');
      console.log(s);
      e.preventDefault();
      $.getJSON(("http://open.mapquestapi.com/geocoding/v1/address?key=Fmjtd%7Cluub2dutn9%2Cbn%3Do5-9u25gr&location=" + s + "&callback=renderGeocode"), function(data) {
        console.log(data);
          var values = {};
              s.each(function() {
                        values[this.name] = $(this).val();
                            });

      });
      return false;
  });
});

function load_people(filters, url) {
  jQuery.getJSON((url + filters), function(data) {
    console.log( "success" );
      jQuery.each(data.objects, function (key, val) {
        var lng = val.location.coordinates[0];
        var lat = val.location.coordinates[1];
        var name = val.first_name + " " + val.last_name;
        var year = val.preferred_class_year;
        var degree1 = val.wesleyan_degree_1_major_1;
        var degree2 = val.wesleyan_degree_1_major_2;
        var degree3 = val.wesleyan_degree_1_major_3;
        var industry = val.industry;
        var city = val.city;
        var state = val.state;
        var country = val.country;
        var marker = new L.marker([lat, lng]);
        // var marker = L.circleMarker([lat, lng], 200)
        marker.bindPopup("<p><b>" + name + "</b>" + " " + year + "</br />" + degree1 + "<br /> " + degree2 + "<br /> " + degree3 + "<br />" + industry + "<br />" + city + ", " + state + ", " + country + "</p>");
        markers.addLayer(marker);
        people.push(val)
      });
    map.addLayer(markers); 
  })
  .done(function(data) {
    console.log( "second success" ); 
    var next = data.meta.next;
    if (next !== null) {
      load_people(next, "");
    }
  })
  .fail(function() { console.log( "error" ); })
  .always(function() { console.log( "complete" ); });
};
