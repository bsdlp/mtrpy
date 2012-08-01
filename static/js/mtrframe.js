$(document).ready(function() {
    $('.mtrWindow').load('/mtrWindowRequest');
});

$("#mtrFormDOIT").click(function() {
    $('.mtrWindow').load('/ipMtrForm/')
})