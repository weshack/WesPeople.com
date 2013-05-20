var markers;
var people = [];

jQuery(document).ready(function($){
  $("#login-toggle").click(function() {
    $('.login-container').slideToggle(300,function(){
      $("#login-toggle").text('LOG IN').stop();
    });
    $('.signup-container').slideToggle(300, function(){
       $("#login-toggle").text('sign up now').stop();
    });
  });
  $("#footer-toggle").click(function(){
    $("#footer").slideToggle(300,function(){
      $("#footer-teaser").css("bottom", "100px");
    });
  });
});

function load_people(url, filters) {
  jQuery.getJSON((url + filters), function(data) {
      jQuery.each(data.objects, function (key, val) {
        var lng = val.location.coordinates[0];
        var lat = val.location.coordinates[1];
        var name = val.first_name + " " + val.last_name;
        var year = val.preferred_class_year;
        var degree1 = val.wesleyan_degree_1_major_1;
        var degree2 = val.wesleyan_degree_1_major_2;
        var degree3 = val.wesleyan_degree_1_major_3;
        var email = val.preferred_email;

        if (degree2 != "") {
          degree1 = degree1 + "<br />" + degree2;
        } 
        if (degree3 !=  "") {
          degree1 = degree1 + "<br />" + degree3;
        }

        if (email != "") {
          email = "<i class='icon-envelope-alt'></i> " + "<a href='mailto:" + email + "'>" + email + "</a>" + "<br />";
        }

        var industry = val.industry;
        if (industry != "") {
          industry = industry + "<br />";
        }
        var city = val.city;
        var state = val.state;
        var country = val.country;
        var marker = new L.marker([lat, lng]);
        // var marker = L.circleMarker([lat, lng], 200)
        //marker.bindPopup("<p><b>" + name + "</b>" + " " + year + "</br />" + degree1 + "<br /> " + industry + "<br />" + city + ", " + state + ", " + country + "</p>");
        marker.bindPopup("<p><b>" + name + "</b><br />" + "<i class='icon-certificate'></i> Class of " + year + "<br />" + email + "<i class='icon-book'></i> " + degree1 +  industry + "<br />" + city + ", " + state + ", " + country + "</p>");
        markers.addLayer(marker);
        people.push(val)
        jQuery("span#num_people").html(people.length);

      });
    map.addLayer(markers); 
  })
  .done(function(data) {
    console.log( "second success" ); 
    if (data.meta) {
      var next = data.meta.next;
    }
    if (next !== null) {
      load_people(next, "");
    }
  })
  .fail(function() { console.log( "error" ); })
  .always(function() { console.log( "complete" ); });
};
