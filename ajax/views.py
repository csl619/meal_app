from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from ingredients.models import Ingredient
from meals.models import MealCategory


# --------------------- INGREDIENT AJAX CALLS ------------------------
# Add ingredient via new meal page
@login_required
def add_ingredient(request):
    ingredient = request.GET.get('item')
    ingredient_present = Ingredient.objects.filter(name=ingredient).exists()
    data = {'exists': ingredient_present}
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


# reload ingredient list once new ingredient is added
@login_required
def update_ingredients(request):
    ingredients = Ingredient.objects.filter(
        related_user=request.user).order_by('name')
    data = {
        'items': '<option value="">---------</option>',
        }
    for ingredient in ingredients:
        data['items'] += (
            f'<option value="{ingredient.pk}">{ingredient.name}</option>')
    return JsonResponse(data)


# Add category via new meal page
@login_required
def add_category(request):
    category = request.GET.get('item')
    category_present = MealCategory.objects.filter(
        name=category, related_user=request.user).exists()
    data = {'exists': category_present}
    if not category_present:
        cat_form = MealCategory(
            name=category,
            related_user=request.user
        )
        cat_form.save()
        data['message'] = (
            f"<i class='fas fa-check-circle mx-2'></i>Category Added - "
            f"{category}")
    else:
        data['message'] = (
            "Cannot add category as there is already a category in the "
            "system with this name.")
    return JsonResponse(data)


# reload ingredient list once new ingredient is added
@login_required
def update_categories(request):
    categories = MealCategory.objects.filter(
        related_user=request.user).order_by('name')
    data = {
        'items': '<option value="">---------</option>',
        }
    for category in categories:
        data['items'] += (
            f'<option value="{category.pk}">{category.name}</option>')
    return JsonResponse(data)
