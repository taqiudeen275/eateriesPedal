# Generated by Django 3.2.13 on 2022-05-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_foodaverageratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodaverageratings',
            name='rate',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
