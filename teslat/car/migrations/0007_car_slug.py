# Generated by Django 5.1 on 2024-10-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(blank=True, max_length=80, null=True),
        ),
    ]
