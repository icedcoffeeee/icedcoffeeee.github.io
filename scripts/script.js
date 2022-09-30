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

