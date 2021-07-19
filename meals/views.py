from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ingredients.forms import NewIngredientForm
from .forms import NewMealForm, ingredient_formset, NewCategoryForm
from .models import MealIngredient, Meal
from .scripts.form_save import meal_form_save, ingredient_save


@login_required
def meal_list(request):
    context = {}
    template_name = 'meals/list.html'
    context['title'] = 'Meals'
    context['mealForm'] = NewMealForm(prefix='meal')
    return render(request, template_name, context)


class MealDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Meal
    template_name = 'meals/meal_detail.html'

    def get_context_data(self, **kwargs):
        meal = Meal.objects.filter(
            id=self.kwargs.get('pk')).first()
        context = super().get_context_data(**kwargs)
        context['title'] = f'{meal} - Details'
        context['meal_ingredients'] = MealIngredient.objects.filter(
            meal_id=meal.id).order_by('name')
        return context


@login_required
def new_meal(request):
    template_name = 'meals/new_meal.html'
    title = 'New Meal'
    if request.method == 'GET':
        mealForm = NewMealForm(
            prefix='meal')
        formset = ingredient_formset(
            queryset=MealIngredient.objects.none(), prefix='ings')
    elif request.method == 'POST':
        formset = ingredient_formset(request.POST, prefix='ings')
        mealForm = NewMealForm(
            request.POST, prefix='meal')
        if mealForm.is_valid() and formset.is_valid():
            meal = meal_form_save(mealForm, request.user)
            ingredient_save(formset, meal.id, request.user)
            messages.success(request, "Meal successfully added.")
            return redirect('meals')
        else:
            print(mealForm.errors)
            print(formset.errors)
    return render(request, template_name, {
        'mealForm': mealForm,
        'ingredientForm': NewIngredientForm(prefix='ing'),
        'categoryForm': NewCategoryForm(prefix='cat'),
        'formset': formset,
        'title': title,
    })


@login_required
def edit_meal(request, pk):
    obj = get_object_or_404(Meal, id=pk)
    template_name = 'meals/new_meal.html'
    title = 'Edit Meal'
    if request.method == 'GET':
        mealForm = NewMealForm(prefix='meal', instance=obj)
        formset = ingredient_formset(
            queryset=MealIngredient.objects.filter(meal_id=obj.id),
            prefix='ings')
    elif request.method == 'POST':
        formset = ingredient_formset(request.POST, prefix='ings')
        mealForm = NewMealForm(
            request.POST or None, prefix='meal', instance=obj)
        if mealForm.is_valid() and formset.is_valid():
            meal = meal_form_save(mealForm, request.user)
            ingredient_save(formset, meal.id, request.user)
            messages.success(request, "Meal successfully added.")
            return redirect('meals')
        else:
            print(mealForm.errors)
            print(formset.errors)
    return render(request, template_name, {
        'mealForm': mealForm,
        'ingredientForm': NewIngredientForm(prefix='ing'),
        'categoryForm': NewCategoryForm(prefix='cat'),
        'formset': formset,
        'title': title,
        'edit': pk,
    })
