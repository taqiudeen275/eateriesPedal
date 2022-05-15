# Generated by Django 3.2.13 on 2022-05-15 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_foodreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodAverageRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='averageRating', to='vendor.food')),
            ],
        ),
    ]
