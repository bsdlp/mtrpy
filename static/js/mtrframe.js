$(document).ready(function() {
    $('.mtrWindow').load('/mtrWindowRequest');
});

/* $("#mtrFormDOIT").click(function() {
    $('.mtrWindow').post('')
}) */

$('#searchForm').submit(function(event) {
    event.preventDefault();
    var $form = $( this ),
    targetIP = $form.find('input[name="hostName"]').val(),
    url = $form.attr('action');
    $.post(url,{hostName: targetIP},function(data){
        $('.mtrWindow').load('/reqForm');
    })
});