# Generated by Django 5.0.2 on 2024-04-26 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("show_cars", "0003_alter_brand_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="car",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="show_cars.car",
            ),
        ),
    ]
