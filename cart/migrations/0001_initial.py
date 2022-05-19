# Generated by Django 3.2.13 on 2022-05-19 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0011_alter_foodreview_rate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.food')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodcart', models.ManyToManyField(related_name='inCart', to='cart.FoodCart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
