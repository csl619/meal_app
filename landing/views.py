from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from scripts.functions import get_date_list

@login_required
def landing_page(request):
    date_list = get_date_list(request.user)
    context = {
        'title': 'Home',
        'dates': date_list
        }
    return render(request, 'landing/home.html', context)
