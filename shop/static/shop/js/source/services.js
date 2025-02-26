$(document).ready(function(){
    star_events();
    $("#batch-print").on("click", function() {
        window.location.href = '/shop/workorder/print_batch/' + $("#batch-input").val() + '/';
    });
    $(".expected-date").on("blur", function() {
        if(this.value!=this.defaultValue){
            // Update service request value
            var id = $(this).data('id');
            var value = this.value;
            $.ajax({
                url: '/drivers/request/edit/' + id + '/',
                type: 'POST',
                data: {'expected_date': value},
                error: function(data) {
                    alert("An error has occurred. " + data);
                },
                success: function(data) {
                    window.location.reload();
                },
            });
        }
    });
});

var in_the_yard_table_options = {

            // Internationalisation. For more info refer to http://datatables.net/manual/i18n
            "language": {
                "aria": {
                    "sortAscending": ": activate to sort column ascending",
                    "sortDescending": ": activate to sort column descending"
                },
                "emptyTable": "No data available in table",
                "info": "Showing _START_ to _END_ of _TOTAL_ entries",
                "infoEmpty": "No entries found",
                "infoFiltered": "(filtered1 from _MAX_ total entries)",
                "lengthMenu": "Show _MENU_ entries",
                "search": "Search:",
                "zeroRecords": "No matching records found"
            },

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js).
            // So when dropdowns used the scrollable div should be removed.
            //"dom": "<'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",

            "bStateSave": false, // save datatable state(pagination, sort, etc) in cookie.

            "columns": [{
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": false
            },
            {
                "orderable": false
            }],
            "lengthMenu": [
                [5, 15, 20, -1],
                [5, 15, 20, "All"] // change per page values here
            ],
            "order": [[ 3, "desc" ], [ 2, "asc" ]],
            // set the initial value
            "pageLength": 20,
            "pagingType": "bootstrap_full_number",
            "language": {
                "search": "Search: ",
                "lengthMenu": "  _MENU_ records",
                "paginate": {
                    "previous":"Prev",
                    "next": "Next",
                    "last": "Last",
                    "first": "First"
                }
            }
        }

var on_the_road_table_options = {

            // Internationalisation. For more info refer to http://datatables.net/manual/i18n
            "language": {
                "aria": {
                    "sortAscending": ": activate to sort column ascending",
                    "sortDescending": ": activate to sort column descending"
                },
                "emptyTable": "No data available in table",
                "info": "Showing _START_ to _END_ of _TOTAL_ entries",
                "infoEmpty": "No entries found",
                "infoFiltered": "(filtered1 from _MAX_ total entries)",
                "lengthMenu": "Show _MENU_ entries",
                "search": "Search:",
                "zeroRecords": "No matching records found"
            },

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js).
            // So when dropdowns used the scrollable div should be removed.
            //"dom": "<'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",

            "bStateSave": false, // save datatable state(pagination, sort, etc) in cookie.

            "columns": [{
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": false
            },
            {
                "orderable": false
            }],
            "lengthMenu": [
                [5, 15, 20, -1],
                [5, 15, 20, "All"] // change per page values here
            ],
            "order": [[ 3, "desc" ], [ 2, "asc" ]],
            // set the initial value
            "pageLength": 20,
            "pagingType": "bootstrap_full_number",
            "language": {
                "search": "Search: ",
                "lengthMenu": "  _MENU_ records",
                "paginate": {
                    "previous":"Prev",
                    "next": "Next",
                    "last": "Last",
                    "first": "First"
                }
            }
        }

function star_events() {
    $(".stars").rating({'min': 0, 'max': 5, 'step': 1, 'size': 'xs', 'showCaption': false});
    $('.stars').on('rating.change', function(event, value, caption) {
        var target = event.target;
        $.ajax({
            url: '/drivers/request/edit/' + target.dataset['requestId'] + '/',
            type: 'POST',
            data: {'stars': value},
            error: function(data) {
                alert("An error has occurred. " + data);
            },
            success: function(data) {
                reset_data(data);
                //window.location.reload();
            },
        });
    });
    $('.stars').on('rating.clear', function(event) {
        var target = event.target;
        $.ajax({
            url: '/drivers/request/edit/' + target.dataset['requestId'] + '/',
            type: 'POST',
            data: {'stars': 0},
            error: function(data) {
                alert("An error has occurred. " + data);
            },
            success: function(data) {
                window.location.reload();
            },
        });
    });
}

function reset_data(data) {
    //Destroy data table if it exists
    var existingTable = $("#inTheYardTable").dataTable();
    if(existingTable != null) {
        existingTable.fnDestroy();
    }

    //Get html for tbody content
    var service_data_html = "";
    for (var i = 0; i < data.length; i++) {
        var c_data = data[i];
        service_data_html += "<tr>";
        service_data_html += "<td>" + c_data.created_by + "</td>";
        service_data_html += "<td>" + c_data.equipment + "</td>";
        service_data_html += "<td>" + c_data.created_at + "</td>";
        service_data_html += "<td>" + "<input type='number' class='stars' value='" + c_data.priority + "' data-request-id='" + c_data.id + "'><span class='hidden'>" + c_data.priority + "</span>" + "</td>";
        var edit_link = '';
        if (c_data.work_order != null) {
            edit_link = "<a href='/shop/workorder/edit/" + c_data.work_order + "/'>Edit</a>"
        }
        else {
            edit_link = "<a href='/shop/workorder/add/?service_request_id=" + c_data.id + "'>Edit</a>"
        }
        on_the_road_link = '<a href="/drivers/move_to_road/' + c_data.id + '/"><i class="fa fa-arrow-circle-down"></i></a>'
        service_data_html += "<td>" + edit_link + " " + on_the_road_link + "</td>";
        service_data_html += "<td>" + "<a href='/shop/services/print/" + c_data.id + "/'>Print</a>" + "</td>";
        service_data_html += "</tr>";
    }
    //Set tbody
    $(".serviceBody").html(service_data_html);

    //Set data table
    $("#inTheYardTable").dataTable(in_the_yard_table_options);

    star_events();
}

var TableManaged = function () {

    var initTable1 = function () {

        var table = $('#inTheYardTable');

        // begin first table
        table.dataTable(in_the_yard_table_options);

        var tableWrapper = jQuery('#inTheYardTable_wrapper');

        tableWrapper.find('.dataTables_length select').addClass("form-control input-xsmall input-inline"); // modify table per page dropdown
    }

    var initTable2 = function () {

        var table = $('#completedServicesTable');

        // begin first table
        table.dataTable({

            // Internationalisation. For more info refer to http://datatables.net/manual/i18n
            "language": {
                "aria": {
                    "sortAscending": ": activate to sort column ascending",
                    "sortDescending": ": activate to sort column descending"
                },
                "emptyTable": "No data available in table",
                "info": "Showing _START_ to _END_ of _TOTAL_ entries",
                "infoEmpty": "No entries found",
                "infoFiltered": "(filtered1 from _MAX_ total entries)",
                "lengthMenu": "Show _MENU_ entries",
                "search": "Search:",
                "zeroRecords": "No matching records found"
            },

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js).
            // So when dropdowns used the scrollable div should be removed.
            //"dom": "<'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",

            "bStateSave": false, // save datatable state(pagination, sort, etc) in cookie.

            "columns": [{
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": false
            }, {
                "orderable": false
            }],
            "lengthMenu": [
                [5, 15, 20, -1],
                [5, 15, 20, "All"] // change per page values here
            ],
            "order": [],
            // set the initial value
            "pageLength": 20,
            "pagingType": "bootstrap_full_number",
            "language": {
                "search": "Search: ",
                "lengthMenu": "  _MENU_ records",
                "paginate": {
                    "previous":"Prev",
                    "next": "Next",
                    "last": "Last",
                    "first": "First"
                }
            }
        });

        var tableWrapper = jQuery('#completedServicesTable_wrapper');

        tableWrapper.find('.dataTables_length select').addClass("form-control input-xsmall input-inline"); // modify table per page dropdown
    }

    var enteredTable = function () {

        var table = $('#enteredServicesTable');

        // begin first table
        table.dataTable({

            // Internationalisation. For more info refer to http://datatables.net/manual/i18n
            "language": {
                "aria": {
                    "sortAscending": ": activate to sort column ascending",
                    "sortDescending": ": activate to sort column descending"
                },
                "emptyTable": "No data available in table",
                "info": "Showing _START_ to _END_ of _TOTAL_ entries",
                "infoEmpty": "No entries found",
                "infoFiltered": "(filtered1 from _MAX_ total entries)",
                "lengthMenu": "Show _MENU_ entries",
                "search": "Search:",
                "zeroRecords": "No matching records found"
            },

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js).
            // So when dropdowns used the scrollable div should be removed.
            //"dom": "<'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",

            "bStateSave": false, // save datatable state(pagination, sort, etc) in cookie.

            "columns": [{
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": false
            }, {
                "orderable": false
            }],
            "lengthMenu": [
                [5, 15, 20, -1],
                [5, 15, 20, "All"] // change per page values here
            ],
            "order": [],
            // set the initial value
            "pageLength": 20,
            "pagingType": "bootstrap_full_number",
            "language": {
                "search": "Search: ",
                "lengthMenu": "  _MENU_ records",
                "paginate": {
                    "previous":"Prev",
                    "next": "Next",
                    "last": "Last",
                    "first": "First"
                }
            }
        });

        var tableWrapper = jQuery('#enteredServicesTable_wrapper');

        tableWrapper.find('.dataTables_length select').addClass("form-control input-xsmall input-inline"); // modify table per page dropdown
    }

    var initTable3 = function () {

        var table = $('#newWorkOrdersTable');

        // begin first table
        table.dataTable({

            // Internationalisation. For more info refer to http://datatables.net/manual/i18n
            "language": {
                "aria": {
                    "sortAscending": ": activate to sort column ascending",
                    "sortDescending": ": activate to sort column descending"
                },
                "emptyTable": "No data available in table",
                "info": "Showing _START_ to _END_ of _TOTAL_ entries",
                "infoEmpty": "No entries found",
                "infoFiltered": "(filtered1 from _MAX_ total entries)",
                "lengthMenu": "Show _MENU_ entries",
                "search": "Search:",
                "zeroRecords": "No matching records found"
            },

            // Uncomment below line("dom" parameter) to fix the dropdown overflow issue in the datatable cells. The default datatable layout
            // setup uses scrollable div(table-scrollable) with overflow:auto to enable vertical scroll(see: assets/global/plugins/datatables/plugins/bootstrap/dataTables.bootstrap.js).
            // So when dropdowns used the scrollable div should be removed.
            //"dom": "<'row'<'col-md-6 col-sm-12'l><'col-md-6 col-sm-12'f>r>t<'row'<'col-md-5 col-sm-12'i><'col-md-7 col-sm-12'p>>",

            "bStateSave": false, // save datatable state(pagination, sort, etc) in cookie.

            "columns": [{
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": true
            }, {
                "orderable": false
            },
            {
                "orderable": false
            }],
            "lengthMenu": [
                [5, 15, 20, -1],
                [5, 15, 20, "All"] // change per page values here
            ],
            "order": [],
            // set the initial value
            "pageLength": 20,
            "pagingType": "bootstrap_full_number",
            "language": {
                "search": "Search: ",
                "lengthMenu": "  _MENU_ records",
                "paginate": {
                    "previous":"Prev",
                    "next": "Next",
                    "last": "Last",
                    "first": "First"
                }
            }
        });

        var tableWrapper = jQuery('#newWorkOrdersTable_wrapper');

        tableWrapper.find('.dataTables_length select').addClass("form-control input-xsmall input-inline"); // modify table per page dropdown
    }

    var initTable4 = function () {

        var table = $('#onTheRoadTable');

        // begin first table
        table.dataTable(on_the_road_table_options);

        var tableWrapper = jQuery('#onTheRoadTable_wrapper');

        tableWrapper.find('.dataTables_length select').addClass("form-control input-xsmall input-inline"); // modify table per page dropdown
    }

    return {

        //main function to initiate the module
        init: function () {
            if (!jQuery().dataTable) {
                return;
            }

            initTable1();
            initTable2();
            initTable3();
            initTable4();
            enteredTable();
        }

    };

}();
