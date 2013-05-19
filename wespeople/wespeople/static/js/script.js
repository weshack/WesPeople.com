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

var people = $.getJSON("/api/geoperson?preferred_class_year=2012", function(data) {
  console.log( "success" );
    $.each(data.objects, function (key, val) {
      lng = val.location.coordinates[0];
      console.log(lng);
      lat = val.location.coordinates[1];
      console.log(lat);
      name = val.name;
      var marker = L.marker([lat, lng]).addTo(map);
      console.log(marker);
    });
})
.done(function() { console.log( "second success" ); })
.fail(function() { console.log( "error" ); })
.always(function() { console.log( "complete" ); });
