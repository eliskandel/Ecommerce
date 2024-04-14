from django.urls import path
from .views import (
    ProductListView,
    ProductDeleteView,
    ProductCreateView,
    ProductUpdateView,
    OrderDeleteView,
    OrderListView,
    OrderUpdateView,
    OrderDeleteView,
    OrderCreateView,
 
    )
urlpatterns = [
    path('',ProductListView.as_view()),
    path('delete/<int:pk>',ProductDeleteView.as_view()),
    path('create/',ProductCreateView.as_view()),
    path('update/<int:pk>/',ProductUpdateView.as_view()),
    path('order/',OrderListView.as_view()),
    path('order/delete/<int:pk>/',OrderDeleteView.as_view()),
    path('order/create/',OrderCreateView.as_view()),
    path('order/update/<int:pk>/',OrderUpdateView.as_view())
]
