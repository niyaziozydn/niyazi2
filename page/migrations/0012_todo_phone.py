# Generated by Django 4.1.7 on 2023-08-21 14:56

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_todo_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
