window.transitionToPage = function (href) {
    document.querySelector('body').style.opacity = 0
    setTimeout(function () {
        window.location.href = href
    }, 500)
}

document.addEventListener('DOMContentLoaded', function (event) {
    document.querySelector('body').style.opacity = 1
})

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

window.makeFullScreen = function (href) {
    document.querySelector("#slide").classList.remove("hover:scale-125");
    document.querySelector("#slide").style.transition = "all 2s";
    document.querySelector("#slide").style.transformOrigin = "top left";
    document.querySelector("#slide").style.scale = 2;
    setTimeout(function () {
        window.location.href = href
    }, 2000)
}