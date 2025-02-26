$(document).ready(function() {
    $('.other-select').append($('<option/>', {
        value: 'Other',
        text : 'Other'
    }));
    $('.other-select').on('change', function(){
        if ($(this).val() == 'Other'){
            $(this).siblings('.other-input').removeClass('hidden');
        }
        else {
            $(this).siblings('.other-input').addClass('hidden');
        }
    });
});

function goBack() {
    window.history.back()
}