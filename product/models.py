from django.db import models
from user.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200, blank=False, null=False)
    description=models.TextField()
    stock_quantity=models.IntegerField(default=0)
    seller=models.ForeignKey(User, on_delete=models.CASCADE)
    rating= models.FloatField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
