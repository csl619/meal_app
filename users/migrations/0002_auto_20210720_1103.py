# Generated by Django 3.0.8 on 2021-07-20 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='takeaway_day',
            new_name='food_order_day',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='takeaway',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='takeaway_amount',
        ),
    ]