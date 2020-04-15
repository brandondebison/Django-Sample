from django.db import models
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=26, unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."