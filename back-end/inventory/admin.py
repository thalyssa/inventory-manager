from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'category', 'expiration_date', 'is_expired', 'finish_date', 'is_finished']
    list_filter = ['category', 'expiration_date', 'is_expired', 'finish_date', 'is_finished']
    search_fields = ['name',]