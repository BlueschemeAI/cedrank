$(document).ready(function() {
    "use strict";
    
    karu_SearchBoxWidth();
    karu_SingleProductSlide();
    karu_RelatedProductSlide()

});

function karu_SearchBoxWidth() {
    var navMetaWidth = $(".nav-main").outerWidth(),
        navActionWidth = $(".nav-actions").outerWidth(),
        navTotalWidth = (navMetaWidth + navActionWidth) + 20;

    var navCollapseWidth = $("#navbarCollapse").outerWidth(),
        searchBoxWidth = navCollapseWidth - navTotalWidth;
    $(".form-searchBox .form-control").css({
        "width": searchBoxWidth
    })
}

function karu_SingleProductSlide() {
    if ($( ".product-slider-for" ).length) {
        $('.product-slider-for').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            draggable: false,
            arrows: false,
            fade: true,
            asNavFor: '.product-slider-nav'
        });
    }
    if ($( ".product-slider-nav" ).length) {
        $('.product-slider-nav').slick({
            vertical: true,
            verticalSwiping: true,
            slidesToShow: 4,
            slidesToScroll: 1,
            asNavFor: '.product-slider-for',
            dots: false,
            focusOnSelect: true
        }); 
    }   
}

function karu_RelatedProductSlide() {
  if ($( ".related-product-slider" ).length) {
    $('.related-product-slider').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        dots: true,
        arrows: false,
        focusOnSelect: false
    }); 
  }
}


/*jQuery(window).scroll(function() {
  if ($(window).scrollTop() > 70) {
      $('.fixed-top').addClass('bg-white navbar-light').removeClass('navbar-dark');
      $('.navbar-brand img').attr('src', 'assets/images/logo.png');
  } else {
      $('.fixed-top').removeClass('bg-white navbar-light').addClass('navbar-dark');
      $('.navbar-brand img').attr('src', 'assets/images/logo-white.png');
  }
});
$(document).ready(function() {
  $(".scroll-on").on('click', function(event) {

    if (this.hash !== "") {
      event.preventDefault();

      
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        window.location.hash = hash;
      });
    } 
  });
});
$('#navbarCollapse').on('show.bs.collapse', function () {
  $(this).closest('body').addClass('navbar-open');
})
$('#navbarCollapse').on('hide.bs.collapse', function () {
  $(this).closest('body').removeClass('navbar-open');
})*/
