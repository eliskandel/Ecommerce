from rest_framework import serializers
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
        fields=['name', 'description', 'stock_quantity']
    
    def create(self, validated_data):
        request=self.context['request']
        product= Product.objects.create(**validated_data, seller=request.user)
        return product
    
    
    
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
    
    
        
class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['product', 'total_amount']
    
    def create(self, validated_data):
        request=self.context['request']
        product_ins=validated_data.pop('product')
        product=[]
        for i in product_ins:
            product.append(i)
        order=Order.objects.create(**validated_data,buyer=request.user)
        order.product.set(product)
        order.save()
        return order
    
    

    
