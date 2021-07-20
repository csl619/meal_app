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

    def get_queryset(self):
        queryset = Meal.objects.all().order_by('name').filter(
                related_user=self.request.user)
        profile = self.request.query_params.get('profile', None)
        if profile is not None:
            queryset = queryset.exclude(last_planned__isnull=True).order_by(
                'last_planned').reverse()[:14]
        return queryset
