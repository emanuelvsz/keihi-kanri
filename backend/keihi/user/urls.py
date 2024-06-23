from user.views import *

from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

urlpatterns = [
    path(
        "health",
        HealthView.as_view(),
        name="test",
    ),
]