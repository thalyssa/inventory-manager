from rest_framework.serializers import ModelSerializer
from .models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'category', 'expiration_date', 'is_expired', 'finish_date', 'is_finished']