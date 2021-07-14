// add ingredient via new meal page
$(document).on('click','a[id^=add_ing_but]', function(event) {
  event.preventDefault()
  var url = $(this).attr("data-url");
  var update_url = $(this).attr("data-update_url");
  var ingredient = $("input[id=id_ing-name]").val();
  if(ingredient != ''){
    $.ajax({
      url: url,
      data: {
        'ing': ingredient,
      },
      success: function (data) {
        if (data.ingredient_exists) {
          $("#ingredient_failed").html(data.message);
          $("#ingredient_failed").removeClass("d-none");
        }
        else {
          $("#ingredient_added").html(data.message);
          $("#ingredient_added").removeClass("d-none");
          $('#newIngredientModal').modal('toggle');
          $.ajax({
            url: update_url,
            success: function (data) {
              var ingredient_drops = $('select[id^=id_ings-][id$=-related_ingredient]')
              for (var i = 0; i < ingredient_drops.length; i++) {
                t = $(ingredient_drops[i]).children("option").filter(":selected").text()
                v = $(ingredient_drops[i]).children("option").filter(":selected").val()
                console.log(t, v)
                $(ingredient_drops[i]).html(data['ingredients']);
                $(ingredient_drops[i]).children("option").filter(":selected").text(t);
                $(ingredient_drops[i]).children("option").filter(":selected").val(v);
              }
              $('.bootstrap-select').find('.selectpicker').selectpicker('refresh');
            }
          });
        }
      }
    });
  }
});
