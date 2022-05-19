# Generated by Django 3.2.13 on 2022-05-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0010_alter_foodaverageratings_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodreview',
            name='rate',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '1 Trash'), (2, '2 Horible'), (3, '3 Terrible'), (4, '4 Manageable'), (5, '5 Good'), (6, '6 Better'), (7, '7 Tasty'), (8, '8 Yummy'), (9, '9 Awesome'), (10, '10 Superb')], null=True),
        ),
    ]
