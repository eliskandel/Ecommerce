from rest_framework import serializers
from .models import Product

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