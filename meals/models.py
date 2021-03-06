from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from ingredients.models import Ingredient
# Create your models here.

from decimal import Decimal


class MealCategory(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date_added = models.DateField(
        verbose_name='Creation Date', auto_now_add=True, auto_now=False)
    related_user = models.ForeignKey(
        User, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Meal Categories"
        ordering = ['name']


class Meal(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date_added = models.DateField(
        verbose_name='Creation Date', auto_now_add=True, auto_now=False)
    related_user = models.ForeignKey(
        User, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')
    related_category = models.ForeignKey(
        MealCategory, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')
    last_planned = models.DateField(
        verbose_name='Last Planned', auto_now_add=False, auto_now=False,
        null=True)
    times_planned = models.PositiveIntegerField(
        blank=False, null=False, default=0)
    prep_time = models.PositiveIntegerField(
        blank=False, null=False, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(360)])
    cook_time = models.PositiveIntegerField(
        blank=False, null=False, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(360)])
    recipe = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Meals"


class MealIngredient(models.Model):
    meal_id = models.ForeignKey(
        Meal, verbose_name='Related Meal',
        on_delete=models.SET_NULL, null=True, related_name='ingredients')
    related_ingredient = models.ForeignKey(
        Ingredient, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')
    amount = models.DecimalField(
        blank=False, max_digits=6, decimal_places=2, null=False,
        default=Decimal('0.00'))

    def __str__(self):
        return str(f'{self.related_ingredient}')

    class Meta:
        verbose_name_plural = "Meal Ingredients"
        ordering = ['related_ingredient']
