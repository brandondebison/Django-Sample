from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=26)
    password = models.CharField(max_length=26)

    def __str__(self):
        return self.username