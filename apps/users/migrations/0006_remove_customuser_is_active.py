# Generated by Django 4.2.3 on 2023-08-25 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_passwordresettoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
    ]
