from django.urls import path
from . import views as meal_views

urlpatterns = [
    path('', meal_views.meal_list, name='meals'),
    path(
        '<int:pk>/', meal_views.MealDetailView.as_view(),
        name='end_client_detail'),
    path(
    'new_meal/', meal_views.new_meal,
    name='new_meal'),
]
