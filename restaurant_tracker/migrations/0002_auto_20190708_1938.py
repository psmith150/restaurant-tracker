# Generated by Django 2.1.3 on 2019-07-09 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='isOpen',
            new_name='is_open',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='isActive',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
