from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, LoanApplication
from .serializers import UserSerializer, LoanApplicationSerializer
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register_user(request):
    data = request.data
    data['password'] = make_password(data['password'])  # Hash password
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def apply_loan(request):
    data = request.data
    serializer = LoanApplicationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Loan application submitted successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_loans(request):
    loans = LoanApplication.objects.all()
    serializer = LoanApplicationSerializer(loans, many=True)
    return Response(serializer.data)

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import LoanApplication
from .serializers import LoanApplicationSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Ensures only authenticated users can access this endpoint
def get_user_loans(request):
    user = request.user
    loans = LoanApplication.objects.filter(user=user)  # Fetch loans specific to the logged-in user
    serializer = LoanApplicationSerializer(loans, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_loan_status(request, loan_id):
    try:
        loan = LoanApplication.objects.get(id=loan_id, user=request.user)
    except LoanApplication.DoesNotExist:
        return Response({"error": "Loan not found"}, status=404)

    data = request.data
    loan.status = data.get('status', loan.status)
    loan.save()

    return Response({"message": "Loan status updated successfully"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_repayment_status(request, loan_id):
    try:
        loan = LoanApplication.objects.get(id=loan_id, user=request.user)
    except LoanApplication.DoesNotExist:
        return Response({"error": "Loan not found"}, status=404)

    return Response({
        "amount": loan.amount,
        "status": loan.status,
        "repayment_period": loan.repayment_period,
    })

from rest_framework.permissions import IsAuthenticated
from .permissions import IsLoanOwner

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsLoanOwner])
def get_loan_detail(request, loan_id):
    loan = LoanApplication.objects.get(id=loan_id)
    serializer = LoanApplicationSerializer(loan)
    return Response(serializer.data)

@api_view(['GET'])
def health_check(request):
    return Response({"status": "Healthy", "time": now().isoformat()})

from rest_framework.pagination import PageNumberPagination

class StandardResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
def list_loans_paginated(request):
    loans = LoanApplication.objects.filter(user=request.user)
    paginator = StandardResultsPagination()
    paginated_loans = paginator.paginate_queryset(loans, request)
    serializer = LoanApplicationSerializer(paginated_loans, many=True)
    return paginator.get_paginated_response(serializer.data)

