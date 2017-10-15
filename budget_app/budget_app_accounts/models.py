from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Account(models.Model):

    user = models.ForeignKey(User, related_name='accounts')
    name = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(default=timezone.now)
    deleted_datetime = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    heading_date = models.CharField(max_length=50, default="Date")
    heading_text = models.CharField(max_length=50, default="Description")
    heading_in = models.CharField(max_length=50, default="Money In")
    heading_out = models.CharField(max_length=50, default="Money Out")
    heading_balance = models.CharField(max_length=50, default="Balance")

    def __str__(self):
        return self.name




class Transaction(models.Model):

    account = models.ForeignKey(
        'budget_app_accounts.Account',
        related_name='transactions',
        )
    created_datetime = models.DateTimeField(default=timezone.now)
    deleted_datetime = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=200)
    verbose_description = models.CharField(max_length=200)
    trans_date = models.DateField()
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    money_in = models.DecimalField(max_digits=8, decimal_places=2)
    money_out = models.DecimalField(max_digits=8, decimal_places=2)
    net_input = models.DecimalField(max_digits=8, decimal_places=2)
    category_pk = models.IntegerField(blank=True, null=True)
    upload_pk = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.account.name, str(self.balance))




class Adjustment(models.Model):

    transaction = models.ForeignKey(
        'budget_app_accounts.Transaction',
        related_name='adjustments',
    )
    created_datetime = models.DateTimeField(default=timezone.now)
    deleted_datetime = models.DateTimeField(blank=True, null=True)
    trans_date = models.DateField()
    net_input = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return '%s %s; %s %s' % (
            str(self.transaction.trans_date),
            str(self.transaction.balance),
            str(self.trans_date),
            str(self.net_input),
            )
