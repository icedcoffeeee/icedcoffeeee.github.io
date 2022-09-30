// Fading between pages
$(function () {
    $('body').hide().fadeIn(500);
    $('a.transitionToPage').click(function () {
        var link = $(this).attr('href');
        $('body').fadeOut(500, function () {
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

// A 'writing' animation
(function ($) {
    function injector(t, splitter, klass, after) {
        var
            a = t.text().split(splitter),
            inject = '';
        if (a.length) {
            $(a).each(function (i, item) {
                inject += '<span class="' + klass + (i + 1) + '">' + item + '</span>' + after
            });
            t.empty().append(inject)
        }
    }
    var methods = {
        init: function () {
            return this.each(function () {
                injector($(this), '', 'char', '')
            })
        },
        words: function () {
            return this.each(function () {
                injector($(this), ' ', 'word', ' ')
            })
        },
        lines: function () {
            return this.each(function () {
                var r = "eefec303079ad17405c889e092e105b0";
                injector($(this).children("br").replaceWith(r).end(), r, 'line', '')
            })
        }
    };
    $.fn.lettering = function (method) {
        if (method && methods[method]) {
            return methods[method].apply(this, [].slice.call(arguments, 1))
        } else if (method === 'letters' || !method) {
            return methods.init.apply(this, [].slice.call(arguments, 0))
        }
        $.error('Method ' + method + ' does not exist on jQuery.lettering');
        return this
    }
})(jQuery);

$(function () {
    var text = $('.write-on-load'),
        length = text.length,
        timeOut,
        character = 0;

    (function typeWriter() {
        timeOut = setTimeout(function () {
            character++;
            var type = text.substring(0, character);
            $('.write-on-load').text(type);
            typeWriter();

            if (character == length) {
                clearTimeout(timeOut);
            }
        }, 200);
    }());
})

// Making scroll a trigger for any actions
const observerOptions = {
    root: null,
    rootMargin: "0px",
    threshold: 0.7
};

const fadeOnIntersect = new IntersectionObserver(
    function (entries, observer) {
        entries.forEach(entry => {
            if (entry.target.style.opacity == 0)
                entry.target.style.opacity = (
                    entry.isIntersecting ? 1 : 0
                )
        });
    },
    observerOptions
);

const expandOnIntersect = new IntersectionObserver(
    function (entries, observer) {
        entries.forEach(entry => {
            intersects = entry.isIntersecting
            maxHeight = entry.target.style.maxHeight
            if (maxHeight == 0 || maxHeight == "0px") {
                entry.target.style.maxHeight = (
                    intersects ? "450px" : 0
                )
                entry.target.children[0].style.scale = (
                    intersects ? 1 : 1.5
                )
            }
        });
    },
    observerOptions
);
