# Generated by Django 5.1 on 2024-09-01 11:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commoditydata',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
