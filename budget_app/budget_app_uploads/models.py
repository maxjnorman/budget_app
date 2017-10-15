from django.db import models
from django.utils import timezone

from .functions import get_archive_date

class Upload(models.Model):

    account = models.ForeignKey(
        'budget_app_accounts.Account',
        related_name='uploads',
        )
    name = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(default=timezone.now)
    deleted_datetime = models.DateTimeField(blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=200)
    upload_file = models.FileField("Upload", upload_to='uploads/')
    archive_date = models.DateField(default=get_archive_date)
