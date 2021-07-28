from rest_framework import permissions, viewsets
from .serializers import (
    IngredientSerializer, MealSerializer, WeekSerializer
    )
from ingredients.models import Ingredient
from meals.models import Meal
from planner.models import Week


class IngredientVS(viewsets.ReadOnlyModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]


class MealVS(viewsets.ReadOnlyModelViewSet):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Meal.objects.all().order_by('name').filter(
                related_user=self.request.user)
        profile = self.request.query_params.get('profile', None)
        if profile is not None:
            queryset = queryset.exclude(last_planned__isnull=True).order_by(
                'last_planned').reverse()[:28]
        return queryset


class WeekVS(viewsets.ReadOnlyModelViewSet):
    serializer_class = WeekSerializer
    queryset = Week.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    name = 'Planned Weeks'

    def get_queryset(self):
        queryset = Week.objects.all().order_by('-date_added').filter(
                related_user=self.request.user)
        return queryset
