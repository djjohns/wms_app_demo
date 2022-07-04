# Generated by Django 3.2.4 on 2021-07-07 02:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0002_verify_customer_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verify',
            name='customer_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
