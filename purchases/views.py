from django.shortcuts import render, redirect
from .models import Purchase
from .forms import PurchaseForm

def purchase_index(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchases/index.html', {'purchases': purchases})

def purchase_add(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Create a new product from the form data
            new_product = form.save()
            return render(request, 'purchases/new_purchases.html', {
                'form': PurchaseForm(),  # Reset the form after successful submission
                'success': True  # Indicate success
            })
        else:
            return render(request, 'purchases/new_purchases.html',{
                'form': PurchaseForm()
            }) 
    else:
        form = PurchaseForm()
        return render(request, 'purchases/new_purchases.html', {
            'form': form
        })




