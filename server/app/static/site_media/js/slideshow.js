$(function() {

	var TRANSITION_PERIOD = 750;
	var SLIDE_INTERVAL = 7500;
	var NUMBER_OF_SLIDES = $('.slideshow-slide').length;
	var selectedSlide = 0;
	var interval;

	$('.slideshow-nav-button').click(function(event) {

		selectSlide($(this).data('number'));
		rotate();
	});

	$('.slideshow-nav-arrow-right').click(function(event) {

		nextSlide();
		rotate();
	});

	$('.slideshow-nav-arrow-left').click(function(event) {

		prevSlide();
		rotate();
	});

	function rotate() {
		
		clearInterval(interval);

		interval = setInterval(function() {

			nextSlide();
		}, SLIDE_INTERVAL);
	}

	function nextSlide() {

		var newNumber = selectedSlide + 1;

		if(newNumber == NUMBER_OF_SLIDES) {

			newNumber = 0;
		}

		selectSlide(newNumber);
	}

	function prevSlide() {

		var newNumber = selectedSlide - 1;

		if(newNumber == -1) {

			newNumber = NUMBER_OF_SLIDES - 1;
		}

		selectSlide(newNumber);
	}

	function selectSlide(number) {

		var slide = $(".slideshow-slide[data-number='" + number + "']");
		var button = $(".slideshow-nav-button[data-number='" + number + "']");

		if(number != selectedSlide) {

			$('.slideshow-slide').fadeOut(TRANSITION_PERIOD);
			slide.fadeIn(TRANSITION_PERIOD);
			$('.slideshow-nav-button').removeClass('slideshow-nav-button-selected');
			button.addClass('slideshow-nav-button-selected');
			selectedSlide = +number;
		}
	}

	function init() {

		$('.slideshow-slide').first().show();
		selectSlide(0);
	}

	init();
	rotate();
});
