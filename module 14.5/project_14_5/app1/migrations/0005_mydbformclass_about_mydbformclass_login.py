# Generated by Django 5.0.2 on 2024-03-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0004_mydbformclass_balance"),
    ]

    operations = [
        migrations.AddField(
            model_name="mydbformclass",
            name="about",
            field=models.TextField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name="mydbformclass",
            name="login",
            field=models.BooleanField(default=True),
        ),
    ]
