from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from inventory.models import Item
from inventory.serializers import ItemSerializer

# List all itens
class itemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# List details about an specific item   
class itemDetail(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Create new item
class newItem(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Update an item
class updateItem(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Delete an item
class deleteItem(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
