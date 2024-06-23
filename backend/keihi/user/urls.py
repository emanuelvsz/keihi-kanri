from user.views import *

from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

urlpatterns = [
    path(
        "test",
        TestView.as_view(),
        name="test",
    ),
]