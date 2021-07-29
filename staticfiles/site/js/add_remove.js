function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}
function cloneMore(selector, prefix) {
    var newElement = $(selector).clone().insertAfter('.form-row:last');
    var total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    newElement.find(':input:not([type=button]):not([type=submit]):not([type=reset]):not([aria-label=Search])').each(function() {
      if ($(this).attr('name') != 'csrfmiddlewaretoken') {
        var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
      }
    });
    newElement.find(':input[type=number]').each(function() {
      if ($(this).attr('name') != 'csrfmiddlewaretoken') {
        var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('0.00').removeAttr('checked');
      }
    });
    newElement.find(':input[type=checkbox]').each(function() {
      if ($(this).attr('name') != 'csrfmiddlewaretoken') {
        var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('off').prop('checked', false);
      }
    });
    newElement.find(':button').each(function() {
        var name = $(this).attr('data-id').replace('-' + (total-1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'data-id': name}).removeAttr('checked');
    });
    newElement.find('script').each(function() {
        var name = $(this).attr('id').replace('-' + (total-1) + '-', '-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'id': name}).removeAttr('checked');
        var text = $(this).text();
        $(this).text(text.replace('-' + (total-1) + '-', '-' + total + '-'));
    });
    if (newElement.find('.custom-file-label').length>0) {
      newElement.find('.custom-file-label')[0].innerHTML = "Choose file"
    }
    div_block = 'div[id^=div_id_' + prefix +']'
    newElement.find(div_block).each(function() {
        var name = $(this).attr('id').replace('-' + (total-1) + '-', '-' + total + '-');
        var id = name;
        $(this).attr({'id': id}).val('').removeAttr('checked');
    });
    ing_div = 'div[id^=' + prefix +'-]'
    newElement.find(ing_div).each(function() {
        var name = $(this).attr('id').replace('-' + (total-1), '-' + total);
        $(this).attr({'id': name}).html('');
    });
    var submit_id = prefix + '_submit-id-'
    newElement.find(':input[id^=' + submit_id + ']').each(function() {
        var name = $(this).attr('id').replace(submit_id + (total-1), submit_id + total);
        var id = name;
        $(this).attr({'id': id});
    });
    $('.form-row:last').find('.bootstrap-select').replaceWith(function() { return $('select', this); });
    newElement.find('.selectpicker').selectpicker('refresh');
    newElement.find('label').each(function() {
        var forValue = $(this).attr('for');
        if (forValue) {
          forValue = forValue.replace('-' + (total-1) + '-', '-' + total + '-');
          $(this).attr({'for': forValue});
        }
    });


    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    getAddRemove(prefix)
    return false;
}
function deleteForm(prefix, btn) {
    var total = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    if (total > 1){
        btn.closest('.form-row').addClass('d-none');
        index_val = btn.attr('id').split('-').slice(-1)[0]
        deleted_id = '#id_' + prefix + '-' + index_val + '-DELETE'
        console.log(deleted_id)
        $(deleted_id).prop('checked', true)
        $(deleted_id).val('on')
        var selector = '#' + String(prefix) + '_forms .form-row'
        var forms = $(selector);
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
            $(forms.get(i)).find(':input').each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
    }
    return false;
}
function getAddRemove(val){
  var cond = '#' + String(val) + '_forms .form-row:not(:last)'
  var conditionRow = $(cond);
  conditionRow.find('.btn.add-form-row').attr('name', '-').val('-')
  .removeClass('btn-success').addClass('btn-danger')
  .removeClass('add-form-row').addClass('remove-form-row')
  .html('<span class="glyphicon glyphicon-minus" aria-hidden="true"></span>');
}
$(document).on('click', '.add-form-row', function(e){
    e.preventDefault();
    var form_type = $(this).attr('id').split('_')[0];
    var selector = '#' + String(form_type) + '_forms .form-row:last'
    cloneMore(selector, form_type);
    return false;
});
$(document).on('click', '.remove-form-row', function(e){
    e.preventDefault();
    var form_type = $(this).attr('id').split('_')[0];
    deleteForm(form_type, $(this));
    return false;
});
$(document).ready( function () {
  var form_group = $(':input[id^=id_][id$=-TOTAL_FORMS]');
  for (var i=0, formCount=form_group.length; i<formCount; i++) {
      var form_type = $(form_group[i]).attr('id').split('_')[1].replace("-TOTAL", "");
      getAddRemove(form_type)
      };

})
