from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm


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
