# Generated by Django 2.1.11 on 2022-01-07 20:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20220107_2005'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietaryRestriction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='auto_lateplates',
            field=models.ManyToManyField(blank=True, to='menu.MealDayTime'),
        ),
        migrations.AlterField(
            model_name='member',
            name='class_year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2100)]),
        ),
        migrations.AddField(
            model_name='member',
            name='dietary_restrictions',
            field=models.ManyToManyField(blank=True, to='home.DietaryRestriction'),
        ),
    ]
