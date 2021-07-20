from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile
from .forms import UserRegisterForm, UserProfileForm
from meals.models import Meal


@login_required
def profile(request):
    user = User.objects.filter(id=request.user.id).first()
    context = {
        'user': user,
        'profile': Profile.objects.filter(user=user).first(),
        'meals': Meal.objects.exclude(last_planned=None).order_by(
            'last_planned').reverse()[:14],
        'title': 'User Profile'
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
