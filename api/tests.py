from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import LoanApplication

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("password123"))

class LoanApplicationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )
        self.loan = LoanApplication.objects.create(
            user=self.user,
            amount=5000,
            repayment_period=12,
            status="Pending"
        )

    def test_loan_creation(self):
        self.assertEqual(self.loan.amount, 5000)
        self.assertEqual(self.loan.status, "Pending")

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import LoanApplication

User = get_user_model()

class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

    def test_user_loans(self):
        LoanApplication.objects.create(user=self.user, amount=5000, repayment_period=12)
        response = self.client.get('/api/v1/loan/list')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)
