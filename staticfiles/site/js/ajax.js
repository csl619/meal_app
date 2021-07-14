$(document).on('click','a[id^=add_ing_but]', function(event) {
  event.preventDefault()
  var url = $(this).attr("data-url");
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
        }
      }
    });
  }
});
