from django.urls import path
from . import views as week_views


urlpatterns = [
    path('', week_views.planned_week_list, name='planned_weeks'),
]
