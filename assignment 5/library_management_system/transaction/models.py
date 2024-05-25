from django.db import models
from account.models import UserAccount
from .constants import TRANSACTION_TYPE


class Transaction(models.Model):
    account = models.ForeignKey(
        UserAccount, related_name="transaction", on_delete=models.CASCADE
    )

    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]
