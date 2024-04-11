from django.urls import path
from .views import (
    ProductListView,
    ProductDeleteView,
    ProductCreateView,
    ProductUpdateView
    )
urlpatterns = [
    path('',ProductListView.as_view()),
    path('delete/',ProductDeleteView.as_view()),
    path('create/',ProductCreateView.as_view()),
    path('update/<int:pk>/',ProductUpdateView.as_view())
]
