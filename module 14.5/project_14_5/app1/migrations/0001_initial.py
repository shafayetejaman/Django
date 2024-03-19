# Generated by Django 5.0.2 on 2024-03-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyDBFormClass",
            fields=[
                ("ID", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=10)),
                ("balance", models.IntegerField(blank=True, null=True)),
                ("about", models.TextField(max_length=50)),
                ("date", models.DateField()),
                ("hour_rate", models.DecimalField(decimal_places=2, max_digits=5)),
                ("email", models.EmailField(max_length=254)),
                ("profile_img", models.FileField(upload_to="static/app1/images/")),
            ],
        ),
    ]
