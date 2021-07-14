from rest_framework import permissions, viewsets
from .serializers import (
    IngredientSerializer, MealSerializer
    )
from ingredients.models import Ingredient
from meals.models import Meal


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
