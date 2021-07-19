// update modal content based on missing item button selected.
$('#ingModelButton, #catModelButton').click( function(event) {
  var url = $(this).attr("data-url");
  var update_url = $(this).attr("data-update-url");
  var sub_type = $(this).attr("data-sub-type");
  $('#po_title').text($('#po_title').text().replace('**placeholder**', sub_type));
  $('#action_text').text($('#action_text').text().replace('**placeholder**', sub_type));
  $('#add_item_but').prop('text', $('#add_item_but').text().replace('**placeholder**', sub_type));
  $('#add_item_but').attr("data-url", url);
  $('#add_item_but').attr("data-update-url", update_url);
  $('#add_item_but').attr("data-sub-type", sub_type);
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
