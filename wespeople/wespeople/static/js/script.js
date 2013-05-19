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

var people = $.getJSON("/api/geoperson", function() {
  console.log( "success" );
})
.done(function() { console.log( "second success" ); })
.fail(function() { console.log( "error" ); })
.always(function() { console.log( "complete" ); });
