from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    category_name = models.CharField(max_length=100)

    def __str__(self):
            return self.category_name

class Product(models.Model):
    slug = models.SlugField(unique=True)
    product_name = models.CharField(max_length=45)
    
    price = models.DecimalField(max_digits=4, decimal_places=0)
    product_class = models.CharField(max_length=15)
    resistant = models.CharField(max_length=15)
    is_allergic = models.CharField(max_length=50) 
    vitality_days = models.DecimalField(max_digits=3, decimal_places=0)
    modify_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

#  class Product(models.Model):
#     slug = models.SlugField()
#     product_name = models.CharField(max_length=100)
#     modify_date = models.DateTimeField(auto_now=True)
#     price = models.FloatField()
#     resistant = models.IntegerField()
#     is_allergic = models.BooleanField()
#     vitality_days = models.IntegerField()   
#     category = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Sales(models.Model):
    slug = models.SlugField(unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    sale_date = models.DateTimeField(auto_now_add=True)

   
# class sales(models.Model):
#     slug = models.SlugField()
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     discount = models.FloatField()
#     total_price = models.FloatField()
#     sale_date = models.DateTimeField(auto_now_add=True)