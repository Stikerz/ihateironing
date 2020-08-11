from django.test import TestCase
from rest_framework import status
from drycleaning.serializers import (LineItemSerializer, ItemSerializer,
                                     OrderSerializer)
from drycleaning.models import Item, Order, LineItem


class TestDryCleaningViews(TestCase):

    def _setup_lineitems(self):
        order1 = Order(customer_name="lannister x")
        order1.save()
        order2 = Order(customer_name="dothraki x")
        order2.save()
        item1 = Item(name="cloak", price=24.99)
        item1.save()
        item2 = Item(name="sweater", price=12.00)
        item2.save()
        LineItem(order_id=order1, item_id=item2, quantity=2).save()
        LineItem(order_id=order2, item_id=item1, quantity=2).save()

    def test_get_order_list(self):
        Order(customer_name="lannister x").save()
        response = self.client.get("/drycleaning/orders/")

        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(orders), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item_list(self):
        Item(name="cloak", price=24.99).save()
        Item(name="sweater", price=12.00).save()
        response = self.client.get("/drycleaning/items/")

        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(items), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lineitem_list(self):
        self._setup_lineitems()
        response = self.client.get("/drycleaning/lineitems/")

        lineitems = LineItem.objects.all()
        serializer = LineItemSerializer(lineitems, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(lineitems), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lineitem_with_id(self):
        self._setup_lineitems()
        orderid = Order.objects.all().first().id
        response = self.client.get(f"/drycleaning/lineitems/?search={orderid}")

        alllineitems = LineItem.objects.all()
        self.assertEqual(len(alllineitems), 2)
        lineitems = LineItem.objects.all().filter(order_id=orderid)
        serializer = LineItemSerializer(lineitems, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(lineitems), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
