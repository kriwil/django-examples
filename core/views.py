from rest_framework import viewsets
from core.serializers import ItemSerializer
from core.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

