# Generated by Django 3.2.4 on 2022-03-12 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20220311_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
