# Generated by Django 4.1.7 on 2023-08-18 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_todo_latitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Longitude',
            field=models.FloatField(blank=True, max_length=250, null=True),
        ),
    ]