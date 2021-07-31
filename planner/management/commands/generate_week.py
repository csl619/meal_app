from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.conf import settings
from django.utils.text import slugify
from django.db.models import Q

from datetime import date, timedelta
from random import choice as rand_choice

from ingredients.models import Ingredient
from meals.models import Meal, MealIngredient
from pdf_files.scripts.templates import week_pdf
from planner.models import Week, WeekDays, WeekIngredient
from planner.scripts.email_comms import send_email
from users.models import Profile
from pprint import pprint


# Command for creating weekly planners for each user on a specified day.


class Command(BaseCommand):
    help = 'Creates weekly planners report for each user and emails.'

    def handle(self, *args, **options):

        def get_users():
            # users = User.objects.filter(profile__food_order_day=date.today().weekday())
            users = User.objects.filter(profile__food_order_day=0)
            return users

        def get_week():
            today = date.today()
            w_start = today + timedelta(days=1)
            week = []
            week_index = 0
            for d in range(0, 7):
                day = w_start + timedelta(d)
                week.append({
                    'day': day.strftime('%A').lower(),
                    'day_index': day.weekday(),
                    'date': day,
                    'week_index': week_index
                })
                week_index += 1
            return week

        def get_week_items(u, w):
            meals = Meal.objects.filter(related_user=u)
            for d in w:
                profile = Profile.objects.filter(user=u).first()
                last_planned = d['date'] - timedelta(days=profile.meal_repeat)
                if meals.filter(
                        Q(last_planned__lt=last_planned) |
                        Q(last_planned__isnull=True),
                        related_category=getattr(profile, d['day'])).exists():
                    selected_meal = rand_choice(list(meals.filter(
                        Q(last_planned__lt=last_planned) |
                        Q(last_planned__isnull=True),
                        related_category=getattr(profile, d['day']))))
                else:
                    selected_meal = meals.filter(related_category=getattr(
                        profile, d['day'])).order_by('times_planned').first()
                meal = meals.filter(id=selected_meal.id).first()
                d['meal'] = meal
                meal.last_planned = d['date']
                meal.times_planned += 1
                meal.save()
            return w

        def process_week(u, week):
            w_start = ''
            w_end = ''
            for day in week:
                if day['week_index'] == 0:
                    w_start = day['date']
                if day['week_index'] == 6:
                    w_end = day['date']
            week_record = Week(
                name=f'Week Ending: {w_end.strftime("%A %d %B %Y")}',
                week_start=w_start,
                week_end=w_end,
                related_user=u
            )
            week_record.save()
            ingredients = {}
            for day in week:
                week_day = WeekDays(
                    related_week=week_record,
                    related_meal=day['meal'],
                    meal_date=day['date'],
                    meal_day=day['day'],
                )
                week_day.save()
                ing_list = MealIngredient.objects.filter(meal_id=day['meal'])
                for ing in ing_list:
                    if ing.related_ingredient.name in ingredients:
                        ingredients[ing.related_ingredient.name]['amount'] += ing.amount
                    else:
                        ingredients[ing.related_ingredient.name] = {
                            'id': ing.related_ingredient.id,
                            'amount': ing.amount,
                            'unit': ing.related_ingredient.get_default_unit_display(),
                        }
            for i in ingredients:
                week_ing = WeekIngredient(
                    week_id=week_record,
                    related_ingredient=Ingredient.objects.filter(
                        id=ingredients[i]['id']).first(),
                    amount=ingredients[i]['amount']
                )
                week_ing.save()
            return week_record

        def get_week_pdf(pk):
            request = HttpRequest()
            request.method = 'GET'
            request.META['SERVER_NAME'] = 'localhost'
            request.META['SERVER_PORT'] = '8000'
            request.META['STATICFILES_DIRS'] = (
                settings.STATICFILES_DIRS)
            request.META['STATIC_URL'] = settings.STATIC_URL
            request.META['STATIC_ROOT'] = settings.STATIC_ROOT
            pdf = week_pdf(request, pk, 'pdf')
            return pdf

        def main():
            users = get_users()
            for u in users:
                week = get_week()
                week_items = get_week_items(u, week)
                pprint(week_items)
                run_week = process_week(u, week_items)
                file = get_week_pdf(run_week.id)
                file_item = {
                    'name': f"{slugify(process_week.name)}.pdf",
                    'file': file,
                    'type': "application/pdf"
                    }
                e = send_email(run_week.id, [file_item], u)
                e.week_planner_email()

        main()

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully created weekly meal planners and emailed to '
                'user email addresses.'))
