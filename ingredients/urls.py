from django.urls import path
from . import views as ingredient_views

urlpatterns = [
    path('', ingredient_views.ingredient_list, name='ingredients'),
    path(
        'new_ingredient/', ingredient_views.new_ingredient,
        name='new_ingredient'),
]
