from django.db import models

# User details model
class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    accountno = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username

# Transaction details model
from datetime import date

class TransactionDetails(models.Model):
    accountno = models.CharField(max_length=20)
    amount = models.IntegerField()  # Use IntegerField for the amount
    date = models.DateField(default=date.today)
    receiveraccountno = models.CharField(max_length=20)

    def __str__(self):
        return f"Transaction for account {self.accountno}"
