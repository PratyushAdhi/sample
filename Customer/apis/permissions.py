from rest_framework import permissions


class IsCustomer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user == obj)


class IsCustomerOfToDo(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user == obj.customer)


class IsAdminUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user.is_admin)
