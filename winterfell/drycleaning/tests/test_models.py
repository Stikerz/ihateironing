from django.test import TestCase
from django.db import IntegrityError
from drycleaning.models import LineItem, Item, Order
from decimal import Decimal


class TestLineItemModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        Order(customer_name="lannister x").save()
        Item(name="cloak", price=24.99).save()
        Item(name="sweater", price=12.00).save()
        Item(name="coat", price=16.36).save()
        Item(name="socks", price=3.56).save()

    def setUp(self):
        self.order = Order.objects.get(id=1)
        self.item1 = Item.objects.get(id=1)

    def test_price_field(self):
        """Price field in LineItem model gets populated automatically after
        save is called """

        lineitem_instance = LineItem(
            order_id=self.order, item_id=self.item1, quantity=3
        )

        self.assertIsNone(lineitem_instance.price)
        lineitem_instance.save()
        self.assertEqual(lineitem_instance.price, round(Decimal(74.97), 2))

    def test_vat_breakdown_property(self):
        """Test LineItem model property .vatbreakdown"""
        item2 = Item.objects.get(id=2)
        item3 = Item.objects.get(id=3)
        item4 = Item.objects.get(id=4)

        LineItem(order_id=self.order, item_id=self.item1, quantity=2).save()
        LineItem(order_id=self.order, item_id=item2, quantity=1).save()
        LineItem(order_id=self.order, item_id=item3, quantity=2).save()
        LineItem(order_id=self.order, item_id=item4, quantity=6).save()

        lineitem_instance = LineItem.objects.all().first()

        expected_vat_breakdown = {
            "NET": round(Decimal(96.72), 2),
            "VAT": round(Decimal(19.34), 2),
            "GROSS": round(Decimal(116.06), 2),
        }
        self.assertEqual(lineitem_instance.vat_breakdown, expected_vat_breakdown)

    def test_unique_constraint(self):
        """Test only instances with unique order_id & item_id can be saved"""
        with self.assertRaises(IntegrityError):
            LineItem(order_id=self.order, item_id=self.item1, quantity=2).save()
            LineItem(order_id=self.order, item_id=self.item1, quantity=2).save()
