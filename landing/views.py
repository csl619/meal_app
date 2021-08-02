from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from scripts.functions import get_date_list
from users.models import Profile


@login_required
def landing_page(request):
    if Profile.objects.filter(user=request.user).first().profile_setup:
        context = {
            'title': 'Home',
            'dates': get_date_list(request.user)
            }
        return render(request, 'landing/home.html', context)
    else:
        return redirect('new_user_setup')
