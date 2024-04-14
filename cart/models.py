from django.db import models
from user.models import User 
from product.models import Product
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    products=models.ManyToManyField(Product, null=True)
    
    def __str__(self) -> str:
        return f'{self.user}\'s Cart'