# Generated by Django 4.1.7 on 2023-08-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
    ]
