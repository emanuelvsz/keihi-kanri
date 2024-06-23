from work.views import *

from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

urlpatterns = [
    path(
        "work",
        WorkView.as_view(),
        name="work",
    ),
]