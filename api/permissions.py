from rest_framework.permissions import BasePermission

class IsLoanOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
