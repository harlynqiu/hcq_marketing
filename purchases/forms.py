from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product_name', 'supplier_name', 'quantity', 'price_per_unit']
