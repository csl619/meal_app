from django.urls import path, include

import api.views as api
from rest_framework import routers, permissions, renderers


class StaffBrowsableAPIMixin:
    def get_renderers(self):
        rends = [renderers.TemplateHTMLRenderer]
        if self.request.user.is_staff:
            rends = [renderers.JSONRenderer, renderers.BrowsableAPIRenderer]
        return [renderer() for renderer in rends]


class CustomAPIRootView(StaffBrowsableAPIMixin, routers.APIRootView):
    permission_classes = (permissions.IsAdminUser,)


class CustomDefaultRouter(routers.DefaultRouter):
    APIRootView = CustomAPIRootView


router = CustomDefaultRouter()  # browseable api

# Ingredient Routes
router.register(r'ingredients', api.IngredientVS, basename='ingredients')

# Meal Routes
router.register(r'meals', api.MealVS, basename='meals')

# Planner Routes
router.register(r'planned_weeks', api.WeekVS, basename='planned_weeks')

urlpatterns = [
    path('', include(router.urls)),
]
