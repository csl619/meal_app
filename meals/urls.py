from django.urls import path
from . import views as meal_views
from pdf_files import views as pdf_views

urlpatterns = [
    path('', meal_views.meal_list, name='meals'),
    path(
        '<int:pk>/pdf/', pdf_views.view_meal_pdf,
        name='meal_pdf'),
    path('<int:pk>/edit/', meal_views.edit_meal, name='edit_meal'),
    path('new_meal/', meal_views.new_meal, name='new_meal'),
]
