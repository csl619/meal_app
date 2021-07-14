from meals.models import Meal, MealIngredient


def meal_form_save(f, u):
    f = f.save(commit=False)
    f.name = " ".join(f.name.split())
    f.related_user = u
    f.save()
    return f


def ingredient_save(formset, f_id, user):
    meal = Meal.objects.filter(id=f_id).first()
    for f in formset:
        if f.cleaned_data != {}:
            if f.cleaned_data.get('DELETE') is True:
                id = f.cleaned_data.get('id')
                if MealIngredient.objects.filter(id=id.id).exists():
                    MealIngredient.objects.filter(id=id.id).delete()
            else:
                form = f.save(commit=False)
                form.meal_id = meal
                form.save()
