from django.urls import path
from . import views as user_views

urlpatterns = [
    path('staff_admin/register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path(
        'update_meal_categories/', user_views.edit_meal_cats,
        name='edit_meal_cats'),
]
