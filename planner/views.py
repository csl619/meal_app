from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def planned_week_list(request):
    context = {}
    template_name = 'planner/list.html'
    context['title'] = 'Planned Weeks'
    return render(request, template_name, context)
