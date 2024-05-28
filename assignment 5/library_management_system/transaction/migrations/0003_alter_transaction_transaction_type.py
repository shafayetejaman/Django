# Generated by Django 5.0.2 on 2024-05-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transaction", "0002_transaction_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_type",
            field=models.IntegerField(
                choices=[(1, "Deposit"), (2, "Return"), (3, "Borrow")], null=True
            ),
        ),
    ]
