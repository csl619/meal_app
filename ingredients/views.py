from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import NewIngredientForm


@login_required
def ingredient_list(request):
    context = {}
    template_name = 'ingredients/list.html'
    context['title'] = 'Ingredients'
    context['ingredientForm'] = NewIngredientForm(prefix='ing')
    return render(request, template_name, context)


@login_required
def new_ingredient(request):
    if request.method == 'POST':
        ingredientForm = NewIngredientForm(
            request.POST, prefix='ing')
        if ingredientForm.is_valid():
            ing_form = ingredientForm.save(commit=False)
            ing_form.related_user = request.user
            ing_form.save()
            messages.success(request, "Ingredient successfully added.")
            # once saved, redirect to list view
            return redirect('ingredients')
        else:
            print(ingredientForm.errors)
            messages.error(
                request, "There is already an ingredient with this name, "
                "please check what has been entered and try again.")
            return render(request, 'ingredients/list.html', {
                'ingredientForm': ingredientForm,
                'title': 'Ingredients',
            })
    else:
        messages.error(
            request, "The page you are looking for is not valid.")
        return redirect('ingredients')
