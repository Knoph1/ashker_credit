from rest_framework import serializers
from .models import User, LoanApplication

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ['id', 'user', 'amount', 'repayment_period', 'status', 'created_at']
