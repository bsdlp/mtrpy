$(window).resize(function(){

        $('.container').css({
                position:'absolute',
                left: ($(window).width() - $('.container').outerWidth())/2,
                top: ($(window).height() - $('.container').outerHeight())/2
        });

});

$(window).resize();

