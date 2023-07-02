from django.db import models
from django.utils import timezone


class SubscribedUsers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
