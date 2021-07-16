// add ingredient or category via new meal page
$(document).on('click','#add_cat_but, #add_ing_but', function(event) {
  event.preventDefault()
  var url = $(this).data("url");
  var update_url = $(this).data("update-url");
  var sub_type = $(this).data("sub-type");
  var failed = '#' + sub_type + '_failed';
  var added = '#' + sub_type + '_added';
  var modal = '#new_' + sub_type + '_modal';
  var {dropdowns, item} = check_category(sub_type)
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
      'item': $("input[id=id_cat-name]")
    }
  }
  else if (sub_type === 'ingredient') {
    return {
      'dropdowns': $('select[id^=id_ings-][id$=-related_ingredient]'),
      'item': $("input[id=id_ing-name]")
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
