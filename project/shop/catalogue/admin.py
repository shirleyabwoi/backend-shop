from django.contrib import admin
from .models import Product
admin.site.register(Product)
from .models import Category
admin.site.register(Category)
from .models import Tag
admin.site.register(Tag)

# Register your models here.
