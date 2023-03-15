from django.db import models
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

from profiles.models import User 
from products.models import Product

class ReviewManager(models.Manager):
    def create_review(self, user, productid, comment, image,parent, helpfull, date):
        for i in [user, productid, comment, image,parent, helpfull, date]:
            if not i:
                raise ValueError('Fields {} required'.format(i))
        review = self.model(user = user, productid = productid, comment=comment, image= image, helpfull = helpfull, date= date)
        review.save(using=self._db)
        return review


class reviews(models.Model):
    '''Reviews model'''
    # userid, comment, size, color, date, productid
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null = True, related_name='children')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    image = models.TextField()
    helpfull = models.IntegerField()
    date = models.DateTimeField()
    objects = ReviewManager()

    
    REQUIRED_FIELDS = ['user', 'productid', 'comment', 'date']
    
    def get_review_user(self):
        return self.user

    def get_review_product(self):
        return self.productid

    def __str__(self):
        return '{} - {}'.format(self.user, self.productid)
