# Generated by Django 3.1.7 on 2022-01-06 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgroombooking',
            name='check_in',
            field=models.DateField(default=datetime.date(2022, 1, 6)),
        ),
        migrations.AlterField(
            model_name='pgroombooking',
            name='homes',
            field=models.CharField(max_length=50),
        ),
    ]