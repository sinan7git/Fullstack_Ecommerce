from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=13)
    description = models.TextField(max_length=255)
    images = models.ImageField(upload_to="products/images/")
    category = models.ForeignKey("ecommers.Category",on_delete=models.CASCADE,null=True)
    is_deleted = models.BooleanField(default=False)
    add_cart = models.BooleanField(default=False)
    
    
    class Meta:
        db_table = "products_product"
        verbose_name_plural = 'Products'
        
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    
    class Meta:
        db_table = "products_category"
    verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name