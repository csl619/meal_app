from users.models import Profile
from planner.models import WeekDays

from datetime import date, timedelta


def get_date_list(u):
    order_day = Profile.objects.filter(user=u).first().food_order_day
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_list = []
    for i in range(0, 7):
        order_check = False
        today_check = False
        day = (week_start + timedelta(days=i))
        week_day = day.strftime('%A')
        if order_day == str(day.weekday()):
            order_check = True
        if today == day:
            today_check = True
        meal = WeekDays.objects.filter(
            meal_date=day, related_week__related_user=u).first()
        week_list.append({
            'date': day,
            'week_day': week_day,
            'today': today_check,
            'order': order_check,
            'meal': meal
        })
    return week_list
