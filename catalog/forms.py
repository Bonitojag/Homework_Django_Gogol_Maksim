from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """
    Форма для созданния или редактирования продукта
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']