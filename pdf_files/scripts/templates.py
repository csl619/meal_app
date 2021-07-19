from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.utils.text import slugify
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from decimal import Decimal, ROUND_DOWN
from os import getenv
from datetime import datetime

from meals.models import (Meal, MealIngredient)


def meal_pdf(request, id, res_type):
    css_file = f'{getenv("DIR_PATH")}/staticfiles/site/css/pa_pdf.css'
    meal = Meal.objects.filter(pk=id).first()
    ingredients = MealIngredient.objects.filter(meal_id=meal)
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = (
        "inline; filename={name}-{type}.pdf".format(
            name=slugify(meal.name),
            type=slugify('meal_card')
        ))
    template = 'meals/meal_pdf.html'
    css_file = 'staticfiles/site/css/pdf.css'
    d = {
        'meal': meal,
        'ingredients': ingredients,
        'site_url': getenv("SITE_URL")}
    html = render_to_string(template, d)
    if res_type == 'pdf':
        response = HTML(
            string=html, base_url=request.build_absolute_uri()).write_pdf(
                font_config=FontConfiguration(), stylesheets=[CSS(css_file)]
                )
    else:
        HTML(
            string=html, base_url=request.build_absolute_uri()).write_pdf(
                response, font_config=FontConfiguration(),
                stylesheets=[CSS(css_file)]
                )
    return response
