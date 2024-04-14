from django.urls import path
from .views import(
    CartCreateView,
    RemoveProductView,
    CartListView,
    UpdateAPIView
)

urlpatterns = [
    path('',CartListView.as_view()),
    path('create/',CartCreateView.as_view()),
    path('remove/<int:pk>/<int:ppk>/', RemoveProductView.as_view()),
    path('update/<int:pk>',UpdateAPIView.as_view())
]
