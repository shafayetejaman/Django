# Generated by Django 5.0.2 on 2024-05-15 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_rename_withdraw_access_transaction_withdraw_access"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="withdraw_access",
        ),
    ]
