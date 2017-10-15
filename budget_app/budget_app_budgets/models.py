from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Budget(models.Model):

    account = models.ForeignKey(
        'budget_app_accounts.Account',
        related_name='budgets',
        )
    name = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(default=timezone.now)
    deleted_datetime = models.DateTimeField(blank=True, null=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    period = IntegerRangeField(min_value=0, max_value=3, default=2)

    def __str__self():
        return self.name

    def period_transform(period):
        period_dict = {
            'DAILY': 0,
            'WEEKLY': 1,
            'MONTHLY': 2,
            'YEARLY': 3,
            '0': 'Daily',
            '1': 'Weekly',
            '2': 'Monthly',
            '3': 'Yearly',
        }
        if str(period).upper() in period_dict.keys():
            return period_dict[str(period).upper()]
        else:
            return 2




class BudgetTransaction(models.Model):

    budget = models.ForeignKey(
        'budget_app_budgets.Budget',
        related_name='transactions',
        )
    created_datetime = models.DateTimeField(default=timezone.now)
    deleted_datetime = models.DateTimeField(blank=True, null=True)
    net_input = models.DecimalField(max_digits=8, decimal_places=2)
    category_pk = models.IntegerField(blank=True, null=True)




class Category(models.Model):

    user = models.ForeignKey(User, related_name='categories')
    name = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(default=timezone.now)
    deleted_datetime = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=150)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
