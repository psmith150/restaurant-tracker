# Generated by Django 2.1.3 on 2019-11-06 22:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_tracker', '0009_auto_20191106_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]