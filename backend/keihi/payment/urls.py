from payment.views import *

from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

urlpatterns = [
    path(
        "payment",
        PaymentView.as_view(),
        name="payment",
    ),
    path(
        "payment/<int:month_id>",
        PaymentByMonthView.as_view(),
        name="payment_by_month"
    )
]