# Generated by Django 5.0.2 on 2024-03-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musician", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="musicians",
            name="instrument_type",
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
