from rest_framework.response import Response
from rest_framework.views import APIView
from daywork.models import Daywork

from drf_yasg.utils import swagger_auto_schema

class DayworkView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        operation_summary="Retorna uma lista de dias trabalhados",
    )
    def get(self, _):
        payments = Daywork.objects.all()
        return Response(payments)

        