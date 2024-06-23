from payment.views import *

from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

urlpatterns = [
    path(
        "daywork",
        PaymentView.as_view(),
        name="daywork",
    ),
]