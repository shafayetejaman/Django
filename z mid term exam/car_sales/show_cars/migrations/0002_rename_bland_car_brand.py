# Generated by Django 5.0.2 on 2024-04-26 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("show_cars", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="car",
            old_name="bland",
            new_name="brand",
        ),
    ]
