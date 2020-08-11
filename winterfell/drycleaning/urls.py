from django.urls import path

from drycleaning.views import OrderAPIView, ItemAPIView, LineItemAPIView

urlpatterns = [
    path("orders/", OrderAPIView.as_view(), name="order_list"),
    path("items/", ItemAPIView.as_view(), name="order_list"),
    path("lineitems/", LineItemAPIView.as_view(), name="order_list"),
]
