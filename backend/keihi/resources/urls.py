from resources.views import *

from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

urlpatterns = [
    path(
        "month",
        MonthView.as_view(),
        name="month",
    ),
]