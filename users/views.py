from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile
from .forms import (
    UserRegisterForm, UserProfileForm, MealCatForm, MealRepeatForm,
    NewProfileForm)
from meals.models import Meal


@login_required
def profile(request):
    user = User.objects.filter(id=request.user.id).first()
    obj = Profile.objects.filter(user=user).first()
    context = {
        'user': user,
        'profile': Profile.objects.filter(user=user).first(),
        'meals': Meal.objects.exclude(last_planned=None).order_by(
            'last_planned').reverse()[:28],
        'title': 'User Profile',
        'repForm': MealRepeatForm(instance=obj)
    }
    template_name = 'users/profile.html'
    return render(request, template_name, context)


@login_required
def register(request):
    if request.method == 'POST':
        uForm = UserRegisterForm(request.POST)
        pForm = UserProfileForm(request.POST)
        if uForm.is_valid() and pForm.is_valid():
            user = uForm.save()
            profile = pForm.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(
                request, "The account has been created successfully! "
                "The user will now be able to log in.")
            return redirect('home')
    else:
        uForm = UserRegisterForm()
        pForm = UserProfileForm()
    return render(
        request, 'users/register.html',
        {'uForm': uForm, 'pForm': pForm, 'title': 'Register'})


@login_required
def new_user_setup(request):
    obj = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        pForm = NewProfileForm(request.POST, instance=obj)
        if pForm.is_valid():
            profile = pForm.save(commit=False)
            profile.user = request.user
            profile.profile_setup = True
            profile.save()
            messages.success(
                request, "Your preferences have been updated.")
            return redirect('profile')
    else:
        pForm = NewProfileForm(instance=obj)
    return render(
        request, 'users/new_profile_setup.html',
        {'pForm': pForm, 'title': 'Profile Setup'})


@login_required
def edit_meal_cats(request):
    user = User.objects.filter(id=request.user.id).first()
    obj = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        mForm = MealCatForm(request.POST, instance=obj)
        if mForm.is_valid():
            profile = mForm.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(
                request, "Categories updated successfully!")
            return redirect('profile')
    else:
        mForm = MealCatForm(instance=obj)
    return render(
        request, 'users/edit_meal_categories.html',
        {'mForm': mForm, 'title': 'Edit User Meal Categories'})
