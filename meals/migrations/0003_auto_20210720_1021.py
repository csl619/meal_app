# Generated by Django 3.0.8 on 2021-07-20 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_auto_20210714_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mealcategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'Meal Categories'},
        ),
        migrations.AlterField(
            model_name='mealingredient',
            name='unit',
            field=models.CharField(choices=[('1', 'item'), ('2', 'millilitre'), ('3', 'pint'), ('4', 'teaspoon'), ('5', 'tablespoon'), ('6', 'gram'), ('7', 'ounce'), ('8', 'piece'), ('9', 'pinch'), ('10', 'cup')], default='1', max_length=2),
        ),
    ]
