from django.urls import path
from . import views

urlpatterns = [
    path('auth/register', views.register_user),
    path('loan/apply', views.apply_loan),
    path('loan/list', views.get_loans),
]

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('auth/register', views.register_user),
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('loan/apply', views.apply_loan),
    path('loan/list', views.get_user_loans),  # User-specific loan query
]

from django.urls import path
from . import views

urlpatterns = [
    path('loan/list', views.get_user_loans),  # URL for listing user loans
]

urlpatterns += [
    path('loan/<int:loan_id>/update', views.update_loan_status),
    path('loan/<int:loan_id>/repayment', views.get_repayment_status),
]

urlpatterns += [
    path('health', views.health_check),
]

urlpatterns += [
    path('loan/paginated', views.list_loans_paginated),
]

from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ashker API",
        default_version='v1',
        description="API documentation for Ashker Credit Solution",
    ),
    public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

INSTALLED_APPS += ['rest_framework.authtoken']
