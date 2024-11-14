from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from .models import Product

from .forms import ProductForm

# Create your views here.
def index(request):
    return render(request, 'products/index.html', {
        'products':Product.objects.all().order_by('id')
    })

def view_product(request, id):
    product = Product.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Create a new product from the form data
            new_product = form.save()
            return render(request, 'products/add.html', {
                'form': ProductForm(),  # Reset the form after successful submission
                'success': True  # Indicate success
            })


            new_product_name = form.cleaned_data['product_name']
            new_product_descript = form.cleaned_data['product_descript']
            new_product_price = form.cleaned_data['product_price']
            new_product_unit = form.cleaned_data['product_unit']
           

            new_product = Product(
                product_name = new_product_name,
                product_descript = new_product_descript, 
                product_price = new_product_price, 
                product_unit = new_product_unit, 
                
            )
            new_product.save()
            return render(request, 'products/add.html',{
                'form' :ProductForm(), 
                'success': True
            })
         
        else:
            return render(request, 'products/add.html',{
                'form': ProductForm()
            }) 
    else:
        form = ProductForm()
        return render(request, 'products/add.html', {
            'form': form
        })