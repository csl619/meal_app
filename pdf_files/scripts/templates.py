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
from planner.models import (Week, WeekDays, WeekIngredient)


def meal_pdf(request, id, res_type):
    meal = Meal.objects.filter(pk=id).first()
    ingredients = MealIngredient.objects.filter(
        meal_id=meal).order_by('related_ingredient__name')
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = (
        "inline; filename={name}-{type}.pdf".format(
            name=slugify(meal.name).replace('-', '_'),
            type=slugify('meal_card')
        ))
    template = 'meals/meal_pdf.html'
    css_file = 'staticfiles/site/css/meal_pdf.css'
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


def week_pdf(request, id, res_type):
    week = Week.objects.filter(pk=id).first()
    ingredients = WeekIngredient.objects.filter(
        week_id=week).order_by('related_ingredient__name')
    meals = WeekDays.objects.filter(related_week=week).order_by('meal_date')
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = (
        "inline; filename={name}-{type}.pdf".format(
            name=slugify(
                f'we_{week.week_end.strftime("%d-%m-%Y")}').replace('-', '_'),
            type=slugify('planned_meals')
        ))
    template = 'planner/week_pdf.html'
    css_file = 'staticfiles/site/css/week_pdf.css'
    d = {
        'week': week,
        'meals': meals,
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
