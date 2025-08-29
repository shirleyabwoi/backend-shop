from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from .cart import Cart

def list_products(request):
    products = Product.objects.all()
    return render(request, "catalogue/product_list.html", {"products": products})
def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "catalogue/product_detail.html", {"product": product})
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "catalogue/product_form.html", {"form": form})

def add_to_cart(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)   
    cart.add(product=product)
    return redirect("cart_detail")
def cart_detail(request):
    cart = Cart(request)
    return render(request, "catalogue/cart.html", {"cart": cart})
def remove_from_cart(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)  
    cart.remove(product)
    return redirect("cart_detail")









