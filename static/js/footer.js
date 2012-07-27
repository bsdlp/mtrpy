/******************************************************
 * jQuery plug-in
 * Easy Pinned Footer
 * Developed by J.P. Given (http://johnpatrickgiven.com)
 * Useage: anyone so long as credit is left alone
 ******************************************************/
(function($) {
    $.fn.pinFooter = function(options) {
        var wH = $(window).height();
        var wW = getWindowWidth();
        var fH = $(this).outerHeight(true);
        var bH = $("body").outerHeight(true);
        var mB = parseInt($("body").css("margin-bottom"));

        if (options == 'relative') {
            if (bH > getWindowHeight()) {
                $(this).css("position", "absolute");
                $(this).css("width", wW + "px");
                $(this).css("top", bH - fH + "px");
                $("body").css("overflow-x", "hidden");
            } else {
                $(this).css("position", "fixed");
                $(this).css("width", wW + "px");
                $(this).css("top", wH - fH + "px");
            }
        } else {
            $(this).css("position", "fixed");
            $(this).css("width", wW + "px");
            $(this).css("top", wH - fH + "px");
            $("body").css("height", (bH + mB) + "px");
        }
    };

    function getWindowHeight() {
        var windowHeight = 0;
        if (typeof(window.innerHeight) == 'number') {
            windowHeight = window.innerHeight;
        }
        else {
            if (document.documentElement && document.documentElement.clientHeight) {
                windowHeight = document.documentElement.clientHeight;
            }
            else {
                if (document.body && document.body.clientHeight) {
                    windowHeight = document.body.clientHeight;
                }
            }
        }
        return windowHeight;
    };

    function getWindowWidth() {
        var windowWidth = 0;
        if (typeof(window.innerWidth) == 'number') {
            windowWidth = window.innerWidth;
        }
        else {
            if (document.documentElement && document.documentElement.clientWidth) {
                windowWidth = document.documentElement.clientWidth;
            }
            else {
                if (document.body && document.body.clientWidth) {
                    windowWidth = document.body.clientWidth;
                }
            }
        }
        return windowWidth;
    };
})(jQuery);​
