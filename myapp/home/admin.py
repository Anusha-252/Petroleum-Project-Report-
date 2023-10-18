from django.contrib import admin

# Register your models here.
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('country', 'product', 'year', 'sales')
