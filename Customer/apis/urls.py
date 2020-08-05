from .views import (CustomerViewSet, ToDoViewSet, CreateUserView)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'todos', ToDoViewSet, basename='todos')


urlpatterns = [
    path('', include(router.urls)),
    path('createcustomer/', CreateUserView.as_view(), name='create-customer'),
]
