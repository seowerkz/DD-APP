$(document).ready(function(){
    //Increment the idle time counter every minute.
    var idleInterval = setInterval(timerIncrement, 60000); // 1 minute

    //Zero the idle timer on mouse movement.
    $(this).mousemove(function (e) {
        idleTime = 0;
    });
    $(this).keypress(function (e) {
        idleTime = 0;
    });

    $("#save").on("click", function(){
        $("#saveOrComplete").val("save");
        $("#workOrderForm").submit();
    });
    $("#complete").on("click", function(){
        var answer = true;
        if( !$("#odometer").val() ) {
            answer = confirm('The odometer has not been entered! Are you sure you want to save and mark complete this work order?')
        }
        if (answer) {
            $("#saveOrComplete").val("complete");
            $("#workOrderForm").submit();
        }
    });
    $("#finish").on("click", function(){
        if( !$("#axonNumber").val() ) {
            alert('You must enter an axon number.');
            $("#axonNumber").focus();
        } else if ( !$("#workOrderReviewed").is(":checked") ) {
          alert('You must have the work order reviewed.');
          $("#workOrderReviewed").focus();
        } else {
          $("#saveOrComplete").val("finish");
          $("#workOrderForm").submit();
        }
    });
    $('#add_more_parts').click(function() {
        cloneMore('div.part-form:last', 'partsused_set');
    });
    $('#add_more_mechanics').click(function() {
        cloneMore('div.mechanic-form:last', 'workordermechanics_set');
    });
    $('.part-select').append($('<option/>', {
        value: 'Other',
        text : 'Other'
    }));
    $('.part-select').on('change', function(){
        if ($(this).val() == 'Other'){
            $(this).siblings('.new-part').removeClass('hidden');
        }
        else {
            $(this).siblings('.new-part').addClass('hidden');
        }
    });
    $('#add_more_work_performed').click(function() {
        cloneMoreCount('div.work_performed-form:last', 'workperformed_set');
    });
    $('#add_more_problems').click(function() {
        cloneMoreCount('div.problem-form:last', 'servicerequestproblem_set');
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
    $(selector).after(newElement);
}

function cloneMoreCount(selector, type) {
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

function timerIncrement() {
    idleTime = idleTime + 1;
    if (idleTime > 4) { // 5 minutes
        $("#save").click();
    }
}
