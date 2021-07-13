from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def landing_page(request):
    context = {
        'title': 'Home',
        }
    return render(request, 'landing/home.html', context)
