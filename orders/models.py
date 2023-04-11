from django.db import models
from profiles import models as User
from products import models as products


class OrdersManager(models.Manager):
    def create_order(self, product, user, status, quant, country,disctrict, city, street, house, appartment):
        for i in [product, user, status, quant, country,disctrict, city, street, house, appartment]:
            if not i:
                raise ValueError('Field {i} required'.format(i))
        product = self.model(product=product, user=user, status=status, quant=quant, country = country,disctrict =disctrict, city= city, street=street, house=house, appartment=appartment)
        product.save(using=self._db)
        return product
    

    
class Orders(models.Model):
    product = models.ForeignKey(products.Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User.User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    quant = models.IntegerField()
    country = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    appartment = models.CharField(max_length=255)

    objects = OrdersManager()

    REQUIRED_FIELDS = ['product', 'user','quant', 'country', 'disctrict', 'city', 'street', 'house', 'appartment']

    def get_order_user(self):
        return self.user
    
    def __str__(self):
        return self.user