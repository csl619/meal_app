# Generated by Django 3.0.8 on 2021-07-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210720_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='food_order_day',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], default='0', max_length=1),
        ),
    ]
