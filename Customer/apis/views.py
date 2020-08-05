from ..models import (ToDo, Customer)
from .serializers import (
    ToDoSerializer, CustomerSerializer, CustomerCreateSerializer)
from .permissions import (IsCustomer, IsCustomerOfToDo)
# libray imports
from rest_framework import (generics, viewsets)
from rest_framework.permissions import (IsAdminUser, IsAuthenticated)


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    permission_classes = [IsAdminUser, IsAuthenticated, IsCustomerOfToDo]

    def get_queryset(self):
        queryset = ToDo.objects.all()
        username = self.request.user
        if username is not None:
            queryset = queryset.filter(customer=username)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        #customer = generics.get_object_or_404(Customer, email=user)
        customer = Customer.objects.filter(email=user)
        item = serializer.save(customer=user)
        if item.priority:
            customer.update(priority=item)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser, IsAuthenticated, IsCustomer]
    lookup_field = 'username'


class CreateUserView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerCreateSerializer
    permission_classses = [IsAdminUser]

    def perform_create(self, serializer):
        #customer = generics.get_object_or_404(Customer, email=user)
        serializer.save(
            email=self.request.data['email'], username=self.request.data['username'], password=self.request.data['password'])
