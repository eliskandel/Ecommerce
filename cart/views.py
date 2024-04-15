from rest_framework.response import Response
from .models import Cart
from product.models import Product
from rest_framework.generics import(
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer,CartWriteSerializer
# Create your views here.
class CartCreateView(CreateAPIView):
    serializer_class=CartWriteSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    

class RemoveProductView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    
    def delete(self, request, pk,ppk ):
        cart_items=Cart.objects.filter(id=pk, user=request.user).first()
        if cart_items:
            product=Product.objects.filter(id=ppk).first()
            if product:
                cart_items.products.remove(product)
                return Response({"message":"Item removed"})
            else:
                return Response({"message":"Item Not found"})
        else:
            return Response({"message":"cart not found"})
    

class CartListView(ListAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
class CartUpdateView(UpdateAPIView):
    queryset=Cart.objects.all()

    serializer_class=CartSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
   
    def get_queryset(self):
       return Cart.objects.filter(user=self.request.user)
   
    



