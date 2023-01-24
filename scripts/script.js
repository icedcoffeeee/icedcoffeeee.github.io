// Fading between pages
$(function () {
  $("body").hide().fadeIn(500);
  $("a.transitionToPage").click(function () {
    var link = $(this).attr("href");
    $("body").fadeOut(500, function () {
      window.location.href = link;
    });
    return false;
  });
});

// Creating shadow under the navigation pane
$(function () {
  var navpane = $("#navpane");
  $(window).scroll(function () {
    var scroll = $(window).scrollTop();

    if (scroll >= 1) {
      navpane.addClass("shadow-xl");
    } else {
      navpane.removeClass("shadow-xl");
    }
  });
});

// Making scroll a trigger for any actions
const observerOptions = {
  root: null,
  rootMargin: "0px",
  threshold: 0.7,
};

const fadeOnIntersect = new IntersectionObserver(function (entries, observer) {
  entries.forEach((entry) => {
    if (entry.isIntersecting)
      entry.target.style.opacity = 1;
  });
}, observerOptions);

const expandOnIntersect = new IntersectionObserver(function (
  entries,
  observer
) {
  entries.forEach((control) => {
    entry = control.target.children[0];
    intersects = control.isIntersecting;
    if (intersects) {
      entry.style.maxHeight = "100%";
      entry.children[0].style.scale = 1;
    }
  });
},
observerOptions);
