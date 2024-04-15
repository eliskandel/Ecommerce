from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from .models import Product,Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

    
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=[
            'name',
            'description',
            'seller',
            'rating'
        ]
    
class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['name', 'description', 'stock_quantity','rating']
    
    def create(self, validated_data):
        request=self.context['request']
        if request.user.category == "seller":
            product= Product.objects.create(**validated_data, seller=request.user)
            return product
        else:
            raise PermissionDenied(detail="User is not a seller")
    
    
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
    def update(self, instance, validated_data):
        
        order=Order.objects.get(buyer=self.user)
        product= validated_data.pop('product')
        order.product.add(product)
        return super().update(instance, validated_data)
    
        
class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['product', 'total_amount']
    
    def create(self, validated_data):
        request=self.context['request']
        order=Order.objects.create(**validated_data,buyer=request.user)
        for product in order.product.all():
            order.product.add(product)
        
        order.save()
        return order
    
    

    
