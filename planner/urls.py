from django.urls import path
from . import views as week_views
from pdf_files import views as pdf_views


urlpatterns = [
    path('', week_views.planned_week_list, name='planned_weeks'),
    path(
        '<int:pk>/pdf/', pdf_views.view_week_pdf,
        name='week_pdf'),
]
