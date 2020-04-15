from django import forms
from .import models

class CreateProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['category','title','slug','description','price','quantity','sku','picture']
