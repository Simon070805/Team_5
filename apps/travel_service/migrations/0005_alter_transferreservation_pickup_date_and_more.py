# Generated by Django 4.2.3 on 2023-08-26 06:28

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_service', '0004_merge_20230825_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferreservation',
            name='pickup_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 26))], verbose_name='Дата получения трансфера'),
        ),
        migrations.AlterField(
            model_name='transferreservation',
            name='return_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 8, 26))], verbose_name='Дата возврата трансфера'),
        ),
    ]
