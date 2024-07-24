from django.db import models
# Create your models here.

class Category(models.Model):

    class Meta:

        db_table = 'category'

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    cor = models.TextField(max_length=200)
    description = models.TextField(null=True, blank=True)
    object3D = models.CharField(max_length=200)

    def str(self):
        return self.title
    
class Products(models.Model):

    class Meta:

        db_table = 'products'

    name = models.CharField(max_length=200)
    imagens = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,null=False, blank=False,related_name="category_products")
    description = models.TextField()

    def str(self):
        return self.name
    
class SubProducts(models.Model):

    class Meta:

        db_table = 'sub_products'

    product_id = models.ForeignKey(Products,on_delete=models.CASCADE,null=False, blank=False,related_name="products_sub_products")
    code = models.CharField(max_length=200)
    bitola = models.CharField(max_length=200)
    embalagem = models.TextField()

    def str(self):
        return self.title
    