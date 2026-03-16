from django.contrib import admin
from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon', 'color')
    search_fields = ('name',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'category', 'transaction_type', 'amount')
    list_filter = ('category', 'transaction_type', 'date')
    search_fields = ('description', 'notes')
    date_hierarchy = 'date'
