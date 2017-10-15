from django.contrib import admin

from .models import Budget, BudgetTransaction, Category

admin.site.register(Budget)
admin.site.register(BudgetTransaction)
admin.site.register(Category)
