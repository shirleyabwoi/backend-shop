from django.urls import path
from .views import list_products, product_detail, create_product, add_to_cart, cart_detail, remove_from_cart

urlpatterns = [
    path('products/', list_products, name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('products/upload/', create_product, name="create_product"),
    path('cart/', cart_detail, name="cart_detail"),
    path('cart/add/<int:id>/', add_to_cart, name="add_to_cart"),
    path('cart/remove/<int:id>/', remove_from_cart, name="remove_from_cart"),
]