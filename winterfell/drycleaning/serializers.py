from rest_framework.serializers import ModelSerializer, ReadOnlyField, DateTimeField

from drycleaning.models import LineItem, Item, Order


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "price"]


class OrderSerializer(ModelSerializer):
    created_at = DateTimeField(format="%d %B %Y")

    class Meta:
        model = Order
        fields = ["id", "customer_name", "created_at"]
        extra_kwargs = {"created_at": {"required": False, "read_only": True}}


class LineItemSerializer(ModelSerializer):
    order_id = OrderSerializer()
    item_id = ItemSerializer()
    vat_breakdown = ReadOnlyField()

    class Meta:
        model = LineItem
        fields = ["id", "order_id", "item_id", "price", "quantity", "vat_breakdown"]
