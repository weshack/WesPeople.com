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
        jQuery("span#num_people").html(people.length);

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
