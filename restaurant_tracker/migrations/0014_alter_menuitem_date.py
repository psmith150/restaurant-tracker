# Generated by Django 5.0 on 2024-02-18 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_tracker', '0013_auto_20220507_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 2, 18, 17, 23, 0, 608211, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
    ]
