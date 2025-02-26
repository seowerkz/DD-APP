$(document).ready(function(){
    $('#add_more_problems').click(function() {
        cloneMore('div.problem-form:last', 'servicerequestproblem_set');
    });
    $('#add_more_images').click(function() {
        $('.fileinput').first().clone().appendTo('#images');
    });
});

function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    newElement.find(".number").text(total);
    $(selector).after(newElement);
}