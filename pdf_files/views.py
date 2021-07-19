from django.contrib.auth.decorators import login_required

from .scripts.templates import (meal_pdf)


@login_required
def view_meal_pdf(request, pk):
    res = meal_pdf(request, pk, 'browser')
    return res
