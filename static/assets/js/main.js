jQuery(function ($) {
	"use strict";
	/**
	 * @param {{alay:string}} data
	 */
	var alay = window.alay || {};
	/*------------------------------------------------------------------
	This file include js code for shortcode, element in main content
	-------------------------------------------------------------------*/
	alay.mainLayoutFuntion = function () {
		$('#totop').on('click', function () {
			$('html, body').animate({ scrollTop: 0 }, 'slow');
			return false;
		});
		$('.search-bar').on('click', function () {
			var input = $(this).next().find('input');
			input.focus();
		});
	};

	// Set menu fixed when scroll
	alay.menuScroll = function () {
		var window_height = $(window).height();
		$(window).bind('scroll load', function () {
			if ($(this).scrollTop() > window_height) {
				$(".sticky-enable header").addClass("header-fixed");
				$(".adminbar-on header").addClass("header-fixed"); // When Admin View
				$('#totop').removeClass('zoomOut');
				$('#totop').addClass('zoomIn');
				$('#totop').fadeIn();
			} else {
				$("header").removeClass("header-fixed");
				$('#totop').addClass('zoomOut');
				$('#totop').removeClass('zoomIn');
				$('#totop').fadeOut();
			}
		});
	};

	// Menu Hover
	alay.menuHover = function () {
		// Dropdown Hover
		$('ul#main-nav li.dropdown').hover(function () {
			var $this = $(this);
			$this.find('.dropdown-menu').show();
			setTimeout(function () {
				$this.addClass('open');
			}, 200)
		}, function () {
			var $this = $(this);
			$this.find('.dropdown-menu').hide();
			setTimeout(function () {
				$this.removeClass('open');
			}, 200)
		});
	};

	// Menu Offcanvas for table and mobile device
	alay.mobileMenu = function () {
		$('.dropdown-toggle > .btn-open-dropdown').on('click', function (e) {
			e.preventDefault();
			e.stopPropagation();
			const menuItem = $(this).parents('.menu-item');
			const submenu = menuItem.find('> .dropdown-menu');

			menuItem.toggleClass('menu-open');
			submenu.toggle();
		});

		$('.open-menuMobile').on('click', function() {
			$('.header-mobile').addClass('show');
			$('.header-mobile-backdrop').addClass('show');
		});

		$('.toggle-header-mobile').on('click', function() {
			$('.header-mobile').removeClass('show');
			$('.header-mobile-backdrop').removeClass('show');
		})

		$('.header-mobile-backdrop').on('click', function() {
			$('.header-mobile').removeClass('show');
			$(this).removeClass('show');
		})
	};

	/*------------------------------------------------------------------
	Initialize Function
	-------------------------------------------------------------------*/
	$(document).ready(function () {
		// Main function
		alay.mainLayoutFuntion();
		alay.menuScroll();

		// Check Menu Style
		if ($(window).width() < 1025) {
			// active offcanvas menu
			alay.mobileMenu();
		} else {
			// active hover menu
			alay.menuHover();
		}

	});
});
