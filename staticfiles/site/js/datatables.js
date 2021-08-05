$(document).ready( function () {
    // INGREDIENT LIST VIEW TABLE STRUCTURE
    $('#ingredient_table').DataTable(
      {
        "dom": "<'row'<'col-sm-6'B><'col-sm-6'f>>" +
               "<'row'<'col-sm-12'tr>>" +
               "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
        "buttons": [
          { 'titleAttr': 'Add Ingredient', "className": 'btn btn-info mr-1', "text": '<i class="fas fa-plus mr-2"></i> Add Ingredient',
                action: function (e, node, config){
                $('#newIngredientModal').modal('toggle')
              }
            },
          { "extend": 'csv', 'titleAttr': 'Export to CSV', "text":'<i class="fas fa-file-csv mr-1"></i> .csv',"className": 'btn btn-light' },
          { "extend": 'excel', 'titleAttr': 'Export to XLSX', "text":'<i class="far fa-file-excel mr-1"></i>.xlsx',"className": 'btn btn-light' },
        ],
        "columns": [
            {"class" : "align-middle pl-2", "data": "name", "name": "name"},
            {"class" : "align-middle text-center", "data": "unit", "name": "unit", "render": function ( data, type, row, meta ) {
                return data+"(s)";
              }},
            {"class" : "align-middle text-center", "data": "date_added", "name": "date_added", 'render': $.fn.dataTable.render.moment('YYYY-MM-DD', 'DD-MMM-YYYY', 'en-gb')},
        ],
        "deferRender": true,
        "scrollX": true,
        "lengthChange": false,
        "paging": true,
        "pageLength": 20,
        "ordering": false,
        "info": false,
        "columnDefs": [
          { "width": "40%", "targets": [0] },
          { "width": "30%", "targets": [1, 2]},
        ],
        "initComplete": function() {
            $(this).show();
            $($.fn.dataTable.tables(true)).DataTable()
            .columns.adjust().draw();
        },
      }
    );
    // MEAL LIST VIEW TABLE STRUCTURE
    $('#meal_table').DataTable(
      {
        "dom": "<'row'<'col-sm-6'B><'col-sm-6'f>>" +
               "<'row'<'col-sm-12'tr>>" +
               "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
        "buttons": [
          { 'titleAttr': 'Add Meal', "className": 'btn btn-info mr-1', "text": '<i class="fas fa-plus mr-2"></i> Add Meal', "action": function ( ) {
                    url = $('#meal_table').data('new_meal');
                    window.location.href = url;
                }
            },
          { "extend": 'csv', 'titleAttr': 'Export to CSV', "text":'<i class="fas fa-file-csv mr-1"></i> .csv',"className": 'btn btn-light' },
          { "extend": 'excel', 'titleAttr': 'Export to XLSX', "text":'<i class="far fa-file-excel mr-1"></i>.xlsx',"className": 'btn btn-light' },
        ],
        "columns": [
            {"class" : "align-middle pl-2", "data": "name", "name": "name"},
            {"class" : "align-middle text-center", "data": "prep_time", "name": "prep_time",
              "render": function ( data, type, row, meta ) {
                return data+"mins";
              }
            },
            {"class" : "align-middle text-center", "data": "cook_time", "name": "cook_time",
              "render": function ( data, type, row, meta ) {
                return data+"mins";
              }
            },
            {"class" : "align-middle text-center", "data": "related_category.name", "name": "related_category.name"},
            {"class" : "align-middle text-center", "data": "last_planned", "name": "last_planned",
              'render': $.fn.dataTable.render.moment('YYYY-MM-DD', 'DD-MMM-YYYY', 'en-gb')},
            {"class" : "align-middle text-center", "data": "date_added", "name": "date_added",
              'render': $.fn.dataTable.render.moment('YYYY-MM-DD', 'DD-MMM-YYYY', 'en-gb')},
            {"class" : "align-middle text-center",
              "data": "id", "name": "id",
              "render": function ( data, type, row, meta ) {
                return "<a class='btn btn-sm btn-secondary' href='/meals/"+data+"/edit/'><i class='far fa-edit mr-1'></i>Edit</a> <a class='btn btn-sm btn-secondary' href='/meals/"+data+"/pdf/' target='_blank'><i class='far fa-file-pdf mr-1'></i>View</a>";
              }
            },
        ],
        "deferRender": true,
        "scrollX": true,
        "lengthChange": false,
        "paging": true,
        "pageLength": 20,
        "ordering": false,
        "info": false,
        "columnDefs": [
          { "width": "30%", "targets": [0] },
          { "width": "10%", "targets": [1,2,3,4,5] },
          { "width": "20%", "targets": [6] },
        ],
        "initComplete": function() {
            $(this).show();
            $($.fn.dataTable.tables(true)).DataTable()
            .columns.adjust().draw();
        },
      }
    );
    // PLANNED WEEK LIST VIEW TABLE STRUCTURE
    $('#week_table').DataTable(
      {
        "dom": "<'row'<'col-sm-6'B><'col-sm-6'f>>" +
               "<'row'<'col-sm-12'tr>>" +
               "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
        "buttons": [
          { "extend": 'csv', 'titleAttr': 'Export to CSV', "text":'<i class="fas fa-file-csv mr-1"></i> .csv',"className": 'btn btn-light' },
          { "extend": 'excel', 'titleAttr': 'Export to XLSX', "text":'<i class="far fa-file-excel mr-1"></i>.xlsx',"className": 'btn btn-light' },
        ],
        "columns": [
            {"class" : "align-middle pl-2", "data": "name", "name": "name"},
            {"class" : "align-middle text-center", "data": "week_start", "name": "week_start",
              'render': $.fn.dataTable.render.moment('YYYY-MM-DD', 'DD-MMM-YYYY', 'en-gb')},
            {"class" : "align-middle text-center", "data": "week_end", "name": "week_end",
              'render': $.fn.dataTable.render.moment('YYYY-MM-DD', 'DD-MMM-YYYY', 'en-gb')},
            {"class" : "align-middle text-center", "data": "date_added", "name": "date_added",
              'render': $.fn.dataTable.render.moment('YYYY-MM-DD', 'DD-MMM-YYYY', 'en-gb')},
            {"class" : "align-middle text-center",
              "data": "id", "name": "id",
              "render": function ( data, type, row, meta ) {
                return "<a class='btn btn-sm btn-secondary' href='/planned_weeks/"+data+"/pdf/' target='_blank'><i class='far fa-file-pdf mr-1'></i>View</a>";
              }
            },
        ],
        "deferRender": true,
        "scrollX": true,
        "lengthChange": false,
        "paging": true,
        "pageLength": 20,
        "ordering": false,
        "info": false,
        "columnDefs": [
          { "width": "40%", "targets": [0] },
          { "width": "15%", "targets": [1,2,3,4] },
        ],
        "initComplete": function() {
            $(this).show();
            $($.fn.dataTable.tables(true)).DataTable()
            .columns.adjust().draw();
        },
      }
    );
    // USER MEAL TABLE STRUCTURE
    $('#user_meal_table').DataTable(
      {
        "dom": "<'row'<'col-sm-6'B><'col-sm-6'f>>" +
               "<'row'<'col-sm-12'tr>>" +
               "<'row'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7'p>>",
        "buttons": {
          "buttons":[
            { "extend": 'csv', 'titleAttr': 'Export to CSV', "text":'<i class="fas fa-file-csv mr-1"></i> .csv',"className": 'btn btn-outline-info' },
            { "extend": 'excel', 'titleAttr': 'Export to XLSX', "text":'<i class="far fa-file-excel mr-1"></i>.xlsx',"className": 'btn btn-outline-info' },

          ],
          'dom': {
            'button': {
              'className': ''
            }
          }
        },
        "columns": [
            {"class" : "align-middle pl-2", "data": "name", "name": "name"},
            {"class" : "align-middle text-center", "data": "prep_time", "name": "prep_time",
              "render": function ( data, type, row, meta ) {
                return data+"mins";
              }
            },
            {"class" : "align-middle text-center", "data": "cook_time", "name": "cook_time",
              "render": function ( data, type, row, meta ) {
                return data+"mins";
              }
            },
            {"class" : "align-middle text-center", "data": "related_category.name", "name": "related_category.name"},
            {"class" : "align-middle text-center", "data": "last_planned", "name": "last_planned",
              'render': $.fn.dataTable.render.moment('YYYY-MM-DD', 'DD-MMM-YYYY', 'en-gb')},
        ],
        "deferRender": true,
        "scrollX": true,
        "lengthChange": false,
        "paging": true,
        "pageLength": 14,
        "ordering": false,
        "info": false,
        "columnDefs": [
          { "width": "60%", "targets": [0] },
          { "width": "10%", "targets": [1,2,3,4] },
        ],
        "initComplete": function() {
            $(this).show();
            $($.fn.dataTable.tables(true)).DataTable()
            .columns.adjust().draw();
        },
      }
    );
    $('a[data-toggle="tab"]').on('shown.bs.tab', function(e){
       $($.fn.dataTable.tables(true)).DataTable()
       .columns.adjust().draw();
    });
});
