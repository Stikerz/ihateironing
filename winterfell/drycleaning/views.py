from rest_framework.generics import ListAPIView
from rest_framework import filters
from drycleaning.models import LineItem, Item, Order
from drycleaning.serializers import OrderSerializer, ItemSerializer, LineItemSerializer


class OrderAPIView(ListAPIView):
    """view for listing a queryset"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ItemAPIView(ListAPIView):
    """view for listing a queryset """

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class LineItemAPIView(ListAPIView):
    """view for listing a queryset """

    queryset = LineItem.objects.all()
    serializer_class = LineItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["order_id__id"]
