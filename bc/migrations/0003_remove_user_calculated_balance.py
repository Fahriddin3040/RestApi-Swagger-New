# Generated by Django 4.2.7 on 2023-11-16 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bc', '0002_user_calculated_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='calculated_balance',
        ),
    ]
