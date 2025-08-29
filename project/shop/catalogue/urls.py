from django.urls import path
from .views import list_products, product_detail, create_product


urlpatterns = [
    path('products/', list_products, name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('products/upload/', create_product, name="create_product"),

]
