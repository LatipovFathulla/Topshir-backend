jQuery(".faq__accordian-heading").click(function (e) {
    e.preventDefault();
    if (!jQuery(this).hasClass("active")) {
      jQuery(".faq__accordian-heading").removeClass("active");
      jQuery(".faq__accordion-content").slideUp(500);
      jQuery(this).addClass("active");
      jQuery(this).next(".faq__accordion-content").slideDown(500);
    } else if (jQuery(this).hasClass("active")) {
      jQuery(this).removeClass("active");
      jQuery(this).next(".faq__accordion-content").slideUp(500);
    }
  });
  // this jQuery codes is used for accordion in faq page