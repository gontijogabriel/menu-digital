from django.db import models
from product.models import Product
from user.models import User


class Order(models.Model):
    order_at = models.DateTimeField(auto_created=True)
    status = models.BooleanField(default=False)
    price = models.FloatField()
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'order' 
        managed = True 
        verbose_name = 'order'
        verbose_name_plural = 'order' 
        
    def __str__(self):
        return f'{self.user}, {self.product}'