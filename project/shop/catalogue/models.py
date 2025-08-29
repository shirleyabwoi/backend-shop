from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=28)
    
class Tag(models.Model):
    name=models.CharField(max_length=28,blank=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    image_url = models.URLField(null=True, blank=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.PROTECT)
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return f"{self.name} price{self.price}"



# Create your models here.
