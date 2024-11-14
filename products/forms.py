from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_descript','product_price','product_unit']
        labels = {
            'product_name': 'Product Name',
            'product_descript': 'Description',
            'product_price': 'Price',
            'product_unit': 'Unit',
            
        }   
        widgets = {
            
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_descript': forms.TextInput(attrs={'class': 'form-control'}),
            'product_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_unit': forms.TextInput(attrs={'class': 'form-control'}),
           
        }


