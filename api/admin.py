from django.contrib import admin
from .models import User, LoanApplication

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'credit_score')
    search_fields = ('username', 'email')

@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'repayment_period', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email')
