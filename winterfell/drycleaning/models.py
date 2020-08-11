from django.db import models
from django.core.validators import MinValueValidator
from django.utils.functional import cached_property
from decimal import Decimal
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):  # pragma: no cover
        return f"{self.name}"


class Order(models.Model):
    customer_name = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):  # pragma: no cover
        return f"{self.customer_name}_{self.id}"


class LineItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.IntegerField(
        null=False, blank=False, validators=[MinValueValidator(1)]
    )

    def save(self, *args, **kwargs):
        unit_price = Item.objects.get(id=self.item_id.id).price
        self.price = unit_price * self.quantity
        super(LineItem, self).save(*args, **kwargs)

    def _tax(self):
        # 20% taxes
        return self._all_lines_total() - self._all_lines_net_total()

    def _all_lines_total(self):
        return (
            LineItem.objects.all()
            .filter(order_id=self.order_id.id)
            .aggregate(models.Sum("price",))["price__sum"]
        )

    def _all_lines_net_total(self):
        return self._all_lines_total() / Decimal(1.2)

    @cached_property
    def vat_breakdown(self):
        net = self._all_lines_net_total()
        vat = self._tax()
        gross = self._all_lines_total()
        return {
            "NET": round(net, 2),
            "VAT": round(vat, 2),
            "GROSS": gross,
        }

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["order_id", "item_id"], name="unique_order")
        ]
