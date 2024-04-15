from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['id','user','products']

    def update(self, instance, validated_data):
        
        return super().update(instance, validated_data)
class CartWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['products']
    
    def create(self, validated_data):
        request=self.context['request']
        user=request.user
        products=validated_data.pop('products')
        cart=Cart.objects.create(**validated_data, user=user)
        for product in products:
            cart.products.add(product)
        cart.save()
        return cart
    


   
    