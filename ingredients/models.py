from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    unit_code = [
        ('1', 'item(s)'),
        ('2', 'millilitre(s)'),
        ('3', 'pint(s)'),
        ('4', 'teaspoon(s)'),
        ('5', 'tablespoon(s)'),
        ('6', 'gram(s)'),
        ('7', 'ounce(s)'),
        ('8', 'piece(s)'),
        ('9', 'pinch(s)'),
        ('10', 'cup(s)'),
        ('11', 'clove(s)'),
    ]

    name = models.CharField(
        verbose_name='Name', max_length=100, blank=False)
    date_added = models.DateField(
        verbose_name='Creation Date', auto_now_add=True, auto_now=False)
    related_user = models.ForeignKey(
        User, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')
    default_unit = models.CharField(
        max_length=2, choices=unit_code, default='1')

    def __str__(self):
        return str(f'{self.name}')

    class Meta:
        verbose_name_plural = "Ingredients"
        ordering = ['name']
