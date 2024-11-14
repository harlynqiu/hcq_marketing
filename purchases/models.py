from django.db import models

class Purchase(models.Model):
    product_name = models.CharField(max_length=100)
    supplier_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} from {self.supplier_name}"