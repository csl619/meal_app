from django.db import models
from django.contrib.auth.models import User

from meals.models import MealCategory


class Profile(models.Model):
    takeaway_options = [
        ('0', 'none'),
        ('1', 'weekly'),
        ('2', 'bi-weekly'),
        ('3', 'once a month'),
        ('4', 'twice a week'),
    ]
    day_code = [
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    takeaway = models.BooleanField(
        verbose_name='Include Takaways', default=False)
    takeaway_amount = models.CharField(
        max_length=1, choices=takeaway_options, default='0')
    takeaway_day = models.CharField(
        max_length=1, choices=day_code, default='1')

    def __str__(self):
        return f'{self.user.username} - Profile'
