from rest_framework import generics
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

# User Registration
@api_view(['POST'])
def register_user(request):
    data = request.data
    user = User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    return Response(UserSerializer(user).data)

# Token Generation
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def obtain_token(request):
    data = request.data
    user = authenticate(username=data['email'], password=data['password'])
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })
    return Response({'error': 'Invalid credentials'}, status=400)

# Product List (For Customers)
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

# Vendor Product Management
class VendorProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(vendor=self.request.user)

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
