from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .scripts.templates import (meal_pdf)
from meals.models import Meal


@login_required
def view_meal_pdf(request, pk):
    obj = get_object_or_404(Meal, id=pk)
    res = meal_pdf(request, pk, 'browser')
    return res
