from rest_framework import serializers

from ingredients.models import Ingredient
from meals.models import Meal
from planner.models import Week


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    unit = serializers.CharField(
        source='get_default_unit_display'
    )

    class Meta:
        model = Ingredient
        fields = '__all__'
        depth = 1


class MealSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Meal
        fields = '__all__'
        depth = 1


class WeekSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Week
        fields = '__all__'
        depth = 1
