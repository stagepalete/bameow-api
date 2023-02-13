from django.db import models
# Create your models here.

class ProductManager(models.Manager):
    # def get_queryset(self):
    #     return super().get_queryset().filter(is_active=True)
    # def create_product(self, name, size):
    #     product = self.model(name = name, size = size)
    #     product.save(using=self._db)
    #     return product
    def create_product(self, name, article, color, size, rating, price, description):
        for i in [name, article, color, size, rating, price, description]:
            if not i:
                raise ValueError('Field {i} required'.format(i))
        product = self.model(name = name, article = article, color = color, size = size, rating = rating, price = price, description = description)
        product.save(using=self._db)
        return product

# 
class Product(models.Model):
    '''Products'''
    name = models.CharField(max_length=500)
    article = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=5)
    rating = models.IntegerField()
    price = models.CharField(max_length=255)
    description = models.TextField()
    objects = ProductManager()

    REQUIRED_FIELDS = ['name', 'article', 'color', 'size', 'rating', 'price', 'description']

    def get_product_name(self):
        return self.name
    

    def __str__(self):
        return self.name