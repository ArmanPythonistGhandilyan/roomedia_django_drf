(function($) {
  
  "use strict";

  // Preloader
  function stylePreloader() {
    $('body').addClass('preloader-deactive');
  }

  // Background Image
  $('[data-bg-img]').each(function() {
    $(this).css('background-image', 'url(' + $(this).data("bg-img") + ')');
  });
  // Background Color
  $('[data-bg-color]').each(function() {
    $(this).css('background-color', $(this).data("bg-color"));
  });
  // Padding Top
  $('[data-padding-top]').each(function() {
    $(this).css('padding-top', $(this).data("padding-top"));
  });

  // Off Canvas JS
  var canvasWrapper = $(".off-canvas-wrapper");
  $(".btn-menu").on('click', function() {
      canvasWrapper.addClass('active');
      $("body").addClass('fix');
  });

  $(".close-action > .btn-close, .off-canvas-overlay").on('click', function() {
      canvasWrapper.removeClass('active');
      $("body").removeClass('fix');
  });

  //Responsive Slicknav JS
  $('.main-menu').slicknav({
      appendTo: '.res-mobile-menu',
      closeOnClick: true,
      removeClasses: true,
      closedSymbol: '<i class="icon_plus"></i>',
      openedSymbol: '<i class="icon_minus-06"></i>'
  });

  // Search Box  JS
  $(".icon-search").on('click', function() {
    $(".btn-search").addClass('show');
    $(".btn-search-content").addClass("show").focus();
  });

  $(".icon-search-close").on('click', function() {
      $(".btn-search").removeClass("show");
      $(".btn-search-content").removeClass("show");
  });

  // Swipper JS
  $(document).ready(function(){

    var testimonialSlider = new Swiper('.testimonial-slider-container', {
      slidesPerView : 1,
      speed: 1000,
      loop: true,
      spaceBetween : 0,
      autoplay: true,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      }
    });

    var testimoniaItemslSlider = new Swiper('.testimonial-items2-slider-container', {
      slidesPerView : 2,
      slidesPerGroup : 1,
      speed: 1000,
      loop: true,
      spaceBetween : 50,
      autoplay: false,
      pagination: {
        el: '.swiper-pagination',
        clickable: true
      },
      breakpoints: {
        1200:{
            slidesPerView : 2,
            spaceBetween : 50
        },

        992:{
            slidesPerView : 2,
            spaceBetween : 30
        },

        768:{
            slidesPerView : 1

        },

        576:{
            slidesPerView : 1
        },

        0:{
            slidesPerView : 1
        }
      }
    });

    var blogSlider = new Swiper('.blog-slider-container', {
      slidesPerView : 3,
      slidesPerGroup : 1,
      speed: 1000,
      loop: true,
      spaceBetween : 30,
      autoplay: false,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      breakpoints: {
        1200:{
            slidesPerView : 3
        },

        992:{
            slidesPerView : 3
        },

        768:{
            slidesPerView : 2

        },

        576:{
            slidesPerView : 1
        },

        0:{
            slidesPerView : 1
        }
      }
    });

    var blogRelatedSlider = new Swiper('.related-post-slider-container', {
      slidesPerView : 2,
      slidesPerGroup : 1,
      speed: 1000,
      loop: true,
      spaceBetween : 30,
      autoplay: false,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      breakpoints: {
        1200:{
            slidesPerView : 2
        },

        992:{
            slidesPerView : 2
        },

        768:{
            slidesPerView : 2

        },

        576:{
            slidesPerView : 1
        },

        0:{
            slidesPerView : 1
        }
      }
    });

    var blogGallerySlider = new Swiper('.post-gallery-slider-container', {
      slidesPerView : 1,
      speed: 1000,
      loop: true,
      spaceBetween : 0,
      autoplay: true,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true
      }
    });

    var brandLogoSlider = new Swiper('.brand-logo-slider-container', {
      slidesPerView : 5,
      loop: true,
      speed: 1000,
      spaceBetween : 30,
      autoplay: false,
      breakpoints: {
        1200:{
            slidesPerView : 5,
            spaceBetween : 125
        },

        992:{
            slidesPerView : 4,
            spaceBetween : 90
        },

        768:{
            slidesPerView : 3,
            spaceBetween : 110

        },

        576:{
            slidesPerView : 3,
            spaceBetween : 60
        },

        380:{
            slidesPerView : 3,
            spaceBetween : 30
        },

        0:{
            slidesPerView : 2,
            spaceBetween : 30
        }
      }
    });

  });

  // Isotope and data filter
  function isotopePortfolio() {
    var $grid = $('.portfolio-grid').isotope({
      itemSelector: '.portfolio-item',
      masonry: {
        columnWidth: 1
      }
    })
    // Isotope Masonry
    var $gridMasonry = $('.portfolio-masonry').isotope({
      itemSelector: '.portfolio-item'
    })
    // Isotope filter Menu
    $('.portfolio-filter-menu').on( 'click', 'button', function() {
      var filterValue = $(this).attr('data-filter');
      $grid.isotope({ filter: filterValue });
      $gridMasonry.isotope({ filter: filterValue });
      $masonryGrid.isotope({ filter: filterValue });
      var filterMenuactive = $(".portfolio-filter-menu button");
      filterMenuactive.removeClass('active');
      $(this).addClass('active');
    });

    // Masonry Grid
    var $masonryGrid = $(".masonryGrid").isotope({
      itemSelector: '.masonry-item'
    });
  }

  // Fancybox Js
  $('.lightbox-image').fancybox();

  //Video Popup
  $('.play-video-popup').fancybox();

  // Scroll Top Hide Show
  $(window).on('scroll', function(){
    if ($(this).scrollTop() > 250) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }

    // Sticky Header
    if($('.sticky-header').length){
      var windowpos = $(this).scrollTop();
      if (windowpos >= 80) {
        $('.sticky-header').addClass('sticky');
      } else {
        $('.sticky-header').removeClass('sticky');
      }
    }
  });

  jQuery(document).ready(function($) {

    // Ajax Contact Form JS
    var form = $('#contact-form');
    var formMessages = $('.form-message');

    $(form).submit(function(e) {
      e.preventDefault();
      var formData = form.serialize();
      $.ajax({
          type: 'POST',
          url: form.attr('action'),
          data: formData
      }).done(function(response) {
          // Make sure that the formMessages div has the 'success' class.
          $(formMessages).removeClass('alert alert-danger');
          $(formMessages).addClass('alert alert-success fade show');

          // Set the message text.
          formMessages.html("<button type='button' class='btn-close' data-bs-dismiss='alert'>&times;</button>");
          formMessages.append(response);

          // Clear the form.
          $('#contact-form input,#contact-form textarea').val('');
      }).fail(function(data) {
          // Make sure that the formMessages div has the 'error' class.
          $(formMessages).removeClass('alert alert-success');
          $(formMessages).addClass('alert alert-danger fade show');

          // Set the message text.
          if (data.responseText !== '') {
              formMessages.html("<button type='button' class='btn-close' data-bs-dismiss='alert'>&times;</button>");
              formMessages.append(data.responseText);
          } else {
              $(formMessages).text('Oops! An error occurred and your message could not be sent.');
          }
      });
    });
  
  });

  // Datepicker
  $( "#datepicker" ).datepicker();

  // Pricing Tab Js
  if ($('#pricing-tab-style').length) {
    var tabSwitch = $('#pricing-tab-style label.switch');
    var TabTitle = $('#pricing-tab-style li');
    var monthTabTitle = $('#pricing-tab-style li.month');
    var annualTabTitle = $('#pricing-tab-style li.annual');
    var monthTabContent = $('#month');
    var annualTabContent = $('#annual');
    monthTabContent.fadeIn();
    annualTabContent.fadeOut();
    function toggleHandle() {
      if (tabSwitch.hasClass('on')) {
        annualTabContent.fadeOut();
        monthTabContent.fadeIn();
        monthTabTitle.addClass('active');
        annualTabTitle.removeClass('active');
      } else {
        monthTabContent.fadeOut();
        annualTabContent.fadeIn();
        annualTabTitle.addClass('active');
        monthTabTitle.removeClass('active');
      }
    };
    monthTabTitle.on('click', function () {
      tabSwitch.addClass('on').removeClass('off');
      toggleHandle();
      return false;
    });
    annualTabTitle.on('click', function () {
      tabSwitch.addClass('off').removeClass('on');
      toggleHandle();
      return false;
    });
    tabSwitch.on('click', function () {
      tabSwitch.toggleClass('on off');
      toggleHandle();
    });
  }
  
  //Counter JS
  var counterId = $('.counter-animate');
  if (counterId.length) {
    counterId.counterUp({
      delay: 10,
      time: 1000
    });
  }

  //Scroll To Top
  $('.scroll-to-top').on('click', function(){
    $('html, body').animate({scrollTop : 0},800);
    return false;
  });

  // Reveal Footer JS
  let revealId = $(".reveal-footer"),
    footerHeight = revealId.outerHeight(),
    windowWidth = $(window).width(),
    windowHeight = $(window).outerHeight();

  if (windowWidth > 991 && windowHeight > footerHeight) {
    $(".site-wrapper-reveal").css({
      'margin-bottom': footerHeight + 'px'
    });
  }
  
  
/* ==========================================================================
   When document is loading, do
   ========================================================================== */
  
  $(window).on('load', function() {
    AOS.init({
      once: true,
    });
    stylePreloader();
    isotopePortfolio();
  });

/* ==========================================================================
   When document is Scrollig, do
   ========================================================================== */
  
  $(window).on('scroll', function() {
  });
  

/* ==========================================================================
   When Window is resizing, do
   ========================================================================== */
  
  $(window).on('resize', function() {
  });
  

})(window.jQuery);

