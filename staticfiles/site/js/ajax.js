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
          setTimeout(function(){$("#ingredient_failed").addClass("d-none")}, 3000);
        }
        else {
          $('#newIngredientModal').modal('toggle');
          $("#ingredient_added").html(data.message);
          $("#ingredient_added").removeClass("d-none");
          setTimeout(function(){$("#ingredient_added").addClass("d-none")}, 3000);
          $.ajax({
            url: update_url,
            success: function (data) {
              var ingredient_drops = $('select[id^=id_ings-][id$=-related_ingredient]')
              for (var i = 0; i < ingredient_drops.length; i++) {
                t = $(ingredient_drops[i]).children("option").filter(":selected").text()
                v = $(ingredient_drops[i]).children("option").filter(":selected").val()
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
$(document).on('click','a[id^=add_cat_but]', function(event) {
  event.preventDefault()
  var url = $(this).attr("data-url");
  var update_url = $(this).attr("data-update_url");
  var category = $("input[id=id_cat-name]").val();
  if(category != ''){
    $.ajax({
      url: url,
      data: {
        'cat': category,
      },
      success: function (data) {
        if (data.category_exists) {
          $("#category_failed").html(data.message);
          $("#category_failed").removeClass("d-none");
          setTimeout(function(){$("#category_failed").addClass("d-none")}, 3000);
        }
        else {
          $('#newCategoryModal').modal('toggle');
          $("#category_added").html(data.message);
          $("#category_added").removeClass("d-none");
          setTimeout(function(){$("#category_added").addClass("d-none")}, 3000);
          $.ajax({
            url: update_url,
            success: function (data) {
              var meal_drops = $('select[id=id_meal-related_category]')
              for (var i = 0; i < meal_drops.length; i++) {
                t = $(meal_drops[i]).children("option").filter(":selected").text()
                v = $(meal_drops[i]).children("option").filter(":selected").val()
                $(meal_drops[i]).html(data['categories']);
                $(meal_drops[i]).children("option").filter(":selected").text(t);
                $(meal_drops[i]).children("option").filter(":selected").val(v);
              }
              $('.bootstrap-select').find('.selectpicker').selectpicker('refresh');
            }
          });
        }
      }
    });
  }
});
