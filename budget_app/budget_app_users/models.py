from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
