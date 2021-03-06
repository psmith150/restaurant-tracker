# Generated by Django 2.1.3 on 2019-11-05 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_tracker', '0005_auto_20190708_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant_tracker.User'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(default=0.0, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(default=0.0, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='price',
            field=models.IntegerField(default=1, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.IntegerField(default=1, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='service',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]
