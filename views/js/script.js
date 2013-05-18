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


