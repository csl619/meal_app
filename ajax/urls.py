from django.urls import path
from . import views


urlpatterns = [
    # Ingredient Ajax Calls
    path(
        'add_ingredient', views.add_ingredient,
        name='ajax_new_ingredient'),
    path(
        'update_ingredients/', views.update_ingredients,
        name='ajax_update_ingredients'),
    path(
        'add_category', views.add_category,
        name='ajax_new_category'),
    path(
        'update_categories/', views.update_categories,
        name='ajax_update_categories'),
]
