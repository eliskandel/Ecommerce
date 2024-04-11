from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,DestroyAPIView,
    CreateAPIView,
    UpdateAPIView
)
from .models import Product
from .serializer import (
    ProductListSerializer,
    ProductSerializer,
    ProductWriteSerializer
    ) 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductListView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductListSerializer
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
    


class ProductDeleteView(DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def get_queryset(self):
        return Product.objects.filter(seller=self.object.user)
    
class ProductCreateView(CreateAPIView):
    serializer_class=ProductWriteSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

class ProductUpdateView(UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    
    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)
        
        
        
        
        