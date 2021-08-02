from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .scripts.templates import Pdf
from meals.models import Meal, MealIngredient
from planner.models import Week, WeekIngredient, WeekDays

from os import getenv


@login_required
def view_meal_pdf(request, pk):
    meal = get_object_or_404(Meal, id=pk)
    template = {
        'template': 'meals/meal_pdf.html',
        'css': 'staticfiles/site/css/meal_pdf.css'
        }
    data_objects = {
        'meal': meal,
        'ingredients': MealIngredient.objects.filter(
            meal_id=meal).order_by('related_ingredient__name'),
    }
    pdf = Pdf(getenv('SITE_URL'), getenv('DIR_PATH'))
    pdf.template(template)
    pdf.context_data(data_objects)
    pdf.name(f'{meal.name}_recipe_card')
    return pdf.generate(request)


@login_required
def view_week_pdf(request, pk):
    week = get_object_or_404(Week, id=pk)
    template = {
        'template': 'planner/week_pdf.html',
        'css': 'staticfiles/site/css/week_pdf.css'
        }
    data_objects = {
        'week': week,
        'ingredients': WeekIngredient.objects.filter(
            week_id=week).order_by('related_ingredient__name'),
        'meals': WeekDays.objects.filter(related_week=week).order_by(
            'meal_date'),
    }
    pdf = Pdf(getenv('SITE_URL'), getenv('DIR_PATH'))
    pdf.template(template)
    pdf.context_data(data_objects)
    pdf.name(f'WE{week.week_end}_planned_meals')
    return pdf.generate(request)
