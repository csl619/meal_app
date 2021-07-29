// update modal content based on missing item button selected.
$('#ingModelButton, #catModelButton').click( function(event) {
  console.log($(this).attr("id"))
  if ($(this).attr("id").includes('ing')) {
    var but = '#add_miss_ing_but'
  }
  else {
    var but = '#add_item_but'
  }
  var url = $(this).attr("data-url");
  var update_url = $(this).attr("data-update-url");
  var sub_type = $(this).attr("data-sub-type");
  $('#po_title').text($('#po_title').text().replace('**placeholder**', sub_type));
  $('#action_text').text($('#action_text').text().replace('**placeholder**', sub_type));
  $(but).prop('text', $(but).text().replace('**placeholder**', sub_type));
  $(but).attr("data-url", url);
  $(but).attr("data-update-url", update_url);
  $(but).attr("data-sub-type", sub_type);
});
// clear modal back to placeholder data ready for next call.
$('#missing_item_modal').on('hidden.bs.modal', function () {
  $('#po_title').text('Add missing **placeholder**');
  $('#action_text').text('Please enter the **placeholder** name:');
  $('#add_item_but').attr("data-url", '');
  $('#add_item_but').attr("data-update-url", '');
  $('#add_item_but').attr("data-sub-type", '');
  $('#add_item_but').prop('text', 'Add **placeholder**');
});
