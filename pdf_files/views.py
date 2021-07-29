from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .scripts.templates import (meal_pdf, week_pdf)
from meals.models import Meal
from planner.models import Week


@login_required
def view_meal_pdf(request, pk):
    obj = get_object_or_404(Meal, id=pk)
    res = meal_pdf(request, pk, 'browser')
    return res


@login_required
def view_week_pdf(request, pk):
    obj = get_object_or_404(Week, id=pk)
    res = week_pdf(request, pk, 'browser')
    return res
