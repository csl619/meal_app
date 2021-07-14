from ingredients.models import Ingredient
from meals.models import Meal
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

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
