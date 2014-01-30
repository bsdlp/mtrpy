$(document).ready(function() {
    $('.mtrWindow').load('/mtrwindow');
});
$(function() {
    $('input#mtrFormDOIT').bind('click', function() {
        $.get('/targetForm', {
            remoteTarget: $('input[name="remoteTarget"]').val()
        }, function(data) {
            $('.mtrWindow').html(data);
        });
        return false;
    });
});

