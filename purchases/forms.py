from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product_name', 'supplier_name', 'quantity', 'price_per_unit']
        labels = {
            'product_name': 'Product Name',
            'supplier_name': 'Supplier Name',
            'quantity': 'Quantity',
            'price_per_unit':'Price per Unit'
            }
        widgets = {
            'product_name':forms.TextInput(attrs={'class': 'form-control'}),
            'supplier_name':forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_per_unit': forms.NumberInput(attrs={'class': 'form-control'}),
        }


