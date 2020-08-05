from ..models import (ToDo, Customer)

from rest_framework import serializers
from django.contrib.auth import authenticate


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
        extra_kwargs = {'priority': {'write_only': True}}


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# class LoginSerializer(serializers.ModelSerializer):

#     email = serializers.EmailField(write_only=True)
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = Customer
#         fields = ['email', 'password']

#     def validate_credential(self, email, password):
#         user = None
#         if email and password:
#             user = authenticate(email=email,
#                                 password=password)
#         else:
#             raise exceptions.ValidationError('Invalid Credentials')
#         return user

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')
#         user = self.validate_credential(email, password)
#         attrs['user'] = user
#         return attrs
