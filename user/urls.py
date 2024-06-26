from django.urls import path
from .views import (
    UserListView,
    UserLoginView,
    UserLogoutView,
    UserCreateView,
    UserDeleteView,
    UserUpdateView
)

urlpatterns = [
    path('',UserListView.as_view()),
    path('login/',UserLoginView.as_view()),
    path('logout/',UserLogoutView.as_view()),
    path('create/',UserCreateView.as_view()),
    path('update/<int:pk>/',UserUpdateView.as_view()),
    path('delete/<int:pk>/',UserDeleteView.as_view()),

]
