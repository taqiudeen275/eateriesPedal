# Generated by Django 3.2.13 on 2022-05-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_alter_vendoracount_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
