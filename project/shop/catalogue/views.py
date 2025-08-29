from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm



def list_products(request):
    products=Product.objects.all()
    return render (request, "catalogue/product_list.html", {"products":products})

def product_detail(request, id):
    product=Product.objects.get(id=id)
    return render (request, "catalogue/product_detail.html", {"product":product})

def create_product(request):
    if request.method == "POST":
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form=ProductForm()
        return render(request, "catalogue/product_form.html", {"form":form})
    
# def add_cart(request, id):
#     product= Product.objects.get(id=id)
#     cart=request.session.get('cart', {})
#     cart[str(product.id)]= cart.get

    

       
       
       
    
    
    

