from django.db import models
from categories.models import Category

# from ..categories.models import Category

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=26,unique=True)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.IntegerField()
    sku = models.IntegerField()
    picture = models.ImageField(default='default.png',blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.description[:150] + "..."

