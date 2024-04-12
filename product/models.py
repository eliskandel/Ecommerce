from django.db import models
from user.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200, blank=False, null=False)
    description=models.TextField()
    stock_quantity=models.IntegerField(default=0)
    seller=models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.FloatField(null=True, blank=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name



class Order(models.Model):
    buyer=models.ForeignKey(User,on_delete=models.CASCADE, related_name="buyer")
    product=models.ManyToManyField(Product, blank=True)
    total_amount=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self) -> str:
        
        return f'{self.buyer} Products'
    
