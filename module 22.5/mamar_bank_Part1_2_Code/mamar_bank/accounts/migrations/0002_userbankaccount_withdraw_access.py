# Generated by Django 5.0.2 on 2024-05-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userbankaccount",
            name="withdraw_access",
            field=models.BooleanField(default=True),
        ),
    ]
