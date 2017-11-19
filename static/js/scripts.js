/*===Drop Down Menu===*/
  jQuery(document).ready(function () {
	 jQuery('.navigation').meanmenu();
	});
/*===Top Fix Navi sticky-navigation===*/	
	 
jQuery(window).on("load", function() {
      jQuery(".navbar-wrapper").sticky({ topSpacing: 0 });
    });
	
/*===animated===*/	
 var wow = new WOW(
  {
    boxClass:     'wow',      // animated element css class (default is wow)
    animateClass: 'animated', // animation css class (default is animated)
    offset:       0,          // distance to the element when triggering the animation (default is 0)
    mobile:       false       // trigger animations on mobile devices (true is default)
  }
  );
  wow.init();
	
	
/*===Back to Top===*/  

     jQuery(window).scroll(function () {
        if (jQuery(this).scrollTop() > 100) {
            jQuery('.scrollup').fadeIn();
        } else {
            jQuery('.scrollup').fadeOut();
        }
    });

    jQuery('.scrollup').click(function () {
        jQuery("html, body").animate({
            scrollTop: 0
        }, 600);
        return false;

});

	//========================
      // Loader
    //========================
jQuery(document).ready(function() {
  jQuery(".owl-carousel").owlCarousel({
    loop: true,
    navigation : true, 
    autoPlay: true,
    autoplayTimeout: 500,
    autoplayHoverPause: true,
    touchDrag: true,
    dots: true,
	 margin:30,
    slideSpeed : 300,
    paginationSpeed : 400,
    singleItem: true,
    pagination: true
  });
});

//========================
// Page Loader
//========================
jQuery(window).load(function () {
    if (jQuery(".container-loader").length > 0)
    {
        jQuery(".container-loader").delay(800).fadeOut("slow");
    }
});
