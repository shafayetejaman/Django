# Generated by Django 5.0.2 on 2024-03-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DBStudent",
            fields=[
                ("name", models.CharField(max_length=50)),
                ("ID", models.IntegerField(primary_key=True, serialize=False)),
                ("email", models.TextField()),
            ],
        ),
    ]