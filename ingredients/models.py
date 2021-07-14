from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Name', max_length=100, blank=False)
    date_added = models.DateField(
        verbose_name='Creation Date', auto_now_add=True, auto_now=False)
    related_user = models.ForeignKey(
        User, blank=True, null=True, default=None,
        on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return str(f'{self.name}')

    class Meta:
        verbose_name_plural = "Ingredients"
        ordering = ['name']
