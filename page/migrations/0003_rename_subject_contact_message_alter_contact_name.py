# Generated by Django 4.1.7 on 2023-08-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='message',
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=158),
        ),
    ]
