// add category via new meal page
$(document).on('click','#add_item_but', function(event) {
  event.preventDefault()
  var url = $('#add_item_but').attr("data-url");
  var update_url = $('#add_item_but').attr("data-update-url");
  var sub_type = $('#add_item_but').attr("data-sub-type");
  var failed = '#add_failed';
  var added = '#' + sub_type + '_added';
  var modal = '#missing_item_modal';
  var item = $("input[id=id-name]")
  var {dropdowns} = check_category(sub_type)
  if(!!item.val()){
    $.ajax({
      url: url,
      data: {
        'item': item.val(),
      },
      success: function (data) {
        if (data.exists) {
          message_wait_and_hide(failed, data.message)
        }
        else {
          message_wait_and_hide(added, data.message)
          $(modal).modal('hide');
          $('#po_title').text($('#po_title').text().replace(sub_type ,'**placeholder**'));
          $('#action_text').text($('#action_text').text().replace(sub_type ,'**placeholder**'));
          $('#add_item_but').prop('text', $('#add_item_but').text().replace(sub_type ,'**placeholder**'));
          $('#add_item_but').attr("data-url", '');
          $('#add_item_but').attr("data-update-url", '');
          $('#add_item_but').attr("data-sub-type", '');
          $(item).val("");
          update_dropdowns(dropdowns, update_url)
        }
      }
    });
  }
});
// add ingredient via new meal page
$(document).on('click','#add_miss_ing_but', function(event) {
  event.preventDefault()
  var url = $('#add_miss_ing_but').attr("data-url");
  var update_url = $('#add_miss_ing_but').attr("data-update-url");
  var sub_type = $('#add_miss_ing_but').attr("data-sub-type");
  var failed = '#add_failed';
  var added = '#' + sub_type + '_added';
  var modal = '#missing_ing_modal';
  var item = $("input[id=ing-name]")
  var unit = $("select[id=ing-default_unit]")
  var {dropdowns} = check_category(sub_type)
  if(!!item.val()){
    $.ajax({
      url: url,
      data: {
        'item': item.val(),
        'unit': unit.val()
      },
      success: function (data) {
        if (data.exists) {
          message_wait_and_hide(failed, data.message)
        }
        else {
          message_wait_and_hide(added, data.message)
          $(modal).modal('hide');
          $('#po_title').text($('#po_title').text().replace(sub_type ,'**placeholder**'));
          $('#action_text').text($('#action_text').text().replace(sub_type ,'**placeholder**'));
          $('#add_miss_ing_but').prop('text', $('#add_miss_ing_but').text().replace(sub_type ,'**placeholder**'));
          $('#add_miss_ing_but').attr("data-url", '');
          $('#add_miss_ing_but').attr("data-update-url", '');
          $('#add_miss_ing_but').attr("data-sub-type", '');
          $(item).val("");
          update_dropdowns(dropdowns, update_url)
        }
      }
    });
  }
});
// function to show message wait 3s and then add d-none class to hide element
function message_wait_and_hide(e, m) {
  $(e).html(m).removeClass("d-none");
  setTimeout(function(){$(e).addClass("d-none")}, 3000);
}
// function to check the category and return the dropdown and item elements
function check_category(sub_type) {
  if (sub_type === 'category') {
    return {
      'dropdowns': $('select[id=id_meal-related_category]'),
    }
  }
  else if (sub_type === 'ingredient') {
    return {
      'dropdowns': $('select[id^=id_ings-][id$=-related_ingredient]'),
    }
  }
}
// function to update dropdowns for changes to ingredient or category list
function update_dropdowns(d, url) {
  $.ajax({
    url: url,
    success: function (data) {
      for (var i = 0; i < d.length; i++) {
        t = $(d[i]).children("option").filter(":selected").text()
        v = $(d[i]).children("option").filter(":selected").val()
        $(d[i]).html(data['items']);
        $(d[i]).children("option").filter(":selected").text(t).val(v);
      }
      $('.bootstrap-select').find('.selectpicker').selectpicker('refresh');
    }
  });
}
// function to update user email address
$(document).on('click','#update_email_but', function(event) {
  event.preventDefault()
  var url = $(this).attr("data-url");
  var email = $("input[id=id-email]").val()
  if(!!email){
    $.ajax({
      url: url,
      data: {
        'email': email,
      },
      success: function (data) {
        location.reload()
      }
    });
  }
});
// function to update user food order day
$(document).on('click','#update_order_day_but', function(event) {
  event.preventDefault()
  var url = $(this).attr("data-url");
  var day = $("select[id=order_day]").val()
  if(!!day){
    $.ajax({
      url: url,
      data: {
        'day': day,
      },
      success: function (data) {
        location.reload()
        $("select[id=order_day]").val('')
      }
    });
  }
});
// function to update user meal repeat
$(document).on('submit','#edit_repeat_form', function(event) {
  event.preventDefault()
  var url = $(this).attr("action");
  var days = $("input[id=id_meal_repeat]").val()
  if(!!days){
    $.ajax({
      url: url,
      data: {
        'days': days,
      },
      success: function (data) {
        location.reload()
      }
    });
  }
});
// function to get selected ingredient unit
$(document).on('change','[id^=id_ings-][id$=-related_ingredient]', function(event) {
  event.preventDefault()
  var url = '/ajax/get_ing_unit/';
  var item = $(this).val()
  var text_field = "#" + $(this).attr("id").replace('-related_ingredient', '').replace('id_', '')
  console.log(text_field)
  if(!!item){
    $.ajax({
      url: url,
      data: {
        'item': item,
      },
      success: function (data) {
         $(text_field).html(data['unit'])
      }
    });
  }
});
