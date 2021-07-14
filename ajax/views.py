from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from ingredients.models import Ingredient


# --------------------- INGREDIENT AJAX CALLS ------------------------
@login_required
def add_ingredient(request):
    ingredient = request.GET.get('ing')
    ingredient_present = Ingredient.objects.filter(name=ingredient).exists()
    data = {'ingredient_exists': ingredient_present}
    if not ingredient_present:
        ing_form = Ingredient(
            name=ingredient,
            related_user=request.user
        )
        ing_form.save()
        data['message'] = (
            f"<i class='fas fa-check-circle mx-2'></i>Ingredient Added - "
            f"{ingredient}")
    else:
        data['message'] = (
            "Cannot add ingredient as there is already an ingredient in the "
            "system with this name.")
    return JsonResponse(data)
