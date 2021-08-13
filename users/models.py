from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from meals.models import MealCategory


class Profile(models.Model):
    day_code = [
        ('0', 'Monday'),
        ('1', 'Tuesday'),
        ('2', 'Wednesday'),
        ('3', 'Thursday'),
        ('4', 'Friday'),
        ('5', 'Saturday'),
        ('6', 'Sunday'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_setup = models.BooleanField(default=False)
    monday = models.ForeignKey(
        MealCategory, verbose_name='Meal Type - Monday',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    tuesday = models.ForeignKey(
        MealCategory, verbose_name='Meal Type - Tuesday',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    wednesday = models.ForeignKey(
        MealCategory, verbose_name='Meal Type - Wednesday',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    thursday = models.ForeignKey(
        MealCategory, verbose_name='Meal Type - Thursday',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    friday = models.ForeignKey(
        MealCategory, verbose_name='Meal Type - Friday',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    saturday = models.ForeignKey(
        MealCategory, verbose_name='Meal Type - Saturday',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    sunday = models.ForeignKey(
        MealCategory, verbose_name='Meal Type - Sunday',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    food_order_day = models.CharField(
        max_length=1, choices=day_code, default='0')
    meal_repeat = models.PositiveIntegerField(
        blank=False, null=False, default=7,
        validators=[MinValueValidator(7), MaxValueValidator(28)],
        help_text=(
            'Changing this value affects how regularly the planner will select'
            ' the same meal. Please choose a value between 7 and 28 days. (The'
            ' default is 7 days (1 week)).'))

    def __str__(self):
        return f'{self.user.username} - Profile'
