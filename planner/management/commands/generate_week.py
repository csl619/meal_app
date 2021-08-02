from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Q

from datetime import date, timedelta
from random import choice as rand_choice

from ingredients.models import Ingredient
from meals.models import Meal, MealIngredient
from pdf_files.scripts.templates import Pdf
from planner.models import Week, WeekDays, WeekIngredient
from planner.scripts.email_comms import Email
from users.models import Profile
from os import getenv


# Command for creating weekly planners for each user on a specified day.


class Command(BaseCommand):
    help = 'Creates weekly planners report for each user and emails.'

    def handle(self, *args, **options):

        class Ingredient_Item:
            def __init__(self, id, amount, unit):
                self.id = id
                self.amount = amount
                self.unit = unit

            def update_amount(self, val):
                self.amount += val

        def get_users():
            users = User.objects.filter(
                profile__food_order_day=date.today().weekday()).exclude(
                    profile__monday=None,
                    profile__tuesday=None,
                    profile__wednesday=None,
                    profile__thursday=None,
                    profile__friday=None,
                    profile__saturday=None,
                    profile__sunday=None
                )
            return users

        def get_week():
            today = date.today()
            w_start = today + timedelta(days=2)
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
            meals_present = False
            if Meal.objects.filter(related_user=u).exists():
                meals_present = True
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
            return w, meals_present



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
            week_ings = {}
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
                    ing_id = ing.related_ingredient.id
                    if ing_id in week_ings:
                        week_ings[ing_id].update_amount(ing.amount)
                    else:
                        week_ings[ing_id] = Ingredient_Item(
                            ing.related_ingredient.id, ing.amount,
                            ing.related_ingredient.get_default_unit_display(),
                        )
            for name, item in week_ings.items():
                week_ing = WeekIngredient(
                    week_id=week_record,
                    related_ingredient=Ingredient.objects.filter(
                        id=item.id).first(),
                    amount=item.amount
                )
                week_ing.save()
            return week_record

        def get_week_pdf(item):
            template = {
                'template': 'planner/week_pdf.html',
                'css': 'staticfiles/site/css/week_pdf.css'
                }
            data_vars = {
                'week': item,
                'ingredients': WeekIngredient.objects.filter(
                    week_id=item).order_by('related_ingredient__name'),
                'meals': WeekDays.objects.filter(related_week=item).order_by(
                    'meal_date'),
            }
            pdf = Pdf(getenv("SITE_URL"), getenv("DIR_PATH"), True)
            pdf.template(template)
            pdf.context_data(data_vars)
            pdf.name(f'WE{item.week_end}_planned_meals')
            return {
                'name': f"Meal_Planner_WE{slugify(item.week_end)}.pdf",
                'file': pdf.generate(),
                'type': "application/pdf"
                }

        def send_email(u, file):
            context_vars = {
                'user': u
            }
            email = Email(
                getenv("ADMIN_HOST"),
                getenv("ADMIN_PORT"),
                getenv("ADMIN_EMAIL"),
                getenv("ADMIN_PASSWORD"),
                getenv("ADMIN_TLS") == 'True',
                getenv("DEBUG_TYPE") == 'True',
                )
            email.subject(
                'Meal Planner | Here are this weeks planned meals!')
            email.body(
                'email_comms/week_planner_email.html', context_vars)
            email.attachments([file])
            email.recipients([u.email])
            email.sender(getenv("ADMIN_EMAIL"))
            email.send()

        def main():
            users = get_users()
            if users:
                for u in users:
                    week = get_week()
                    week_items, meals_present = get_week_items(u, week)
                    if meals_present:
                        run_week = process_week(u, week_items)
                        file = get_week_pdf(run_week)
                        send_email(u, file)
                self.stdout.write(
                    self.style.SUCCESS(
                        'Successfully created weekly meal planners and '
                        'emailed to user email addresses.'))
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        'No users in the system for the current day, proceses '
                        'halted.'))

        main()
