from django.db import models
from django.contrib.auth.models import User

from meals.models import Meal
from ingredients.models import Ingredient

from decimal import Decimal


class Week(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date_added = models.DateField(
        verbose_name='Creation Date', auto_now_add=True, auto_now=False)
    week_start = models.DateField(
        verbose_name='Week Start', auto_now_add=False, auto_now=False)
    week_end = models.DateField(
        verbose_name='Week Start', auto_now_add=False, auto_now=False)
    related_user = models.ForeignKey(
        User, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class WeekDays(models.Model):
    date_added = models.DateField(
        verbose_name='Creation Date', auto_now_add=True, auto_now=False)
    related_week = models.ForeignKey(
        Week, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')
    related_meal = models.ForeignKey(
        Meal, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')
    meal_date = models.DateField(
        verbose_name='Date', auto_now_add=False, auto_now=False, null=True)
    meal_day = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.related_meal.name

    class Meta:
        verbose_name_plural = "Meals"


class WeekIngredient(models.Model):
    week_id = models.ForeignKey(
        Week, verbose_name='Related Meal',
        on_delete=models.SET_NULL, null=True)
    related_ingredient = models.ForeignKey(
        Ingredient, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')
    amount = models.DecimalField(
        blank=False, max_digits=6, decimal_places=2, null=False,
        default=Decimal('0.00'))
