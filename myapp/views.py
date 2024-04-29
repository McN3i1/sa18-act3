from django.shortcuts import render, get_object_or_404
from .models import Product

def product_index(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_index.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myapp/product_detail.html', {'product': product})
