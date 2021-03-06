"""meal_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from landing.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='home'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ajax/', include('ajax.urls')),
    path('api/', include('api.urls')),
    path('user/', include('users.urls')),
    path('ingredients/', include('ingredients.urls')),
    path('meals/', include('meals.urls')),
    path('planned_weeks/', include('planner.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
