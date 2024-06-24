from rest_framework.response import Response
from rest_framework.views import APIView
from resources.serializers import MonthSerializer
from resources.services import MonthServices

from drf_yasg.utils import swagger_auto_schema


class MonthView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        operation_summary="Retorna uma lista de meses do ano",
    )
    def get(self, _):
        payments = MonthServices.get_all()
        serializer = MonthSerializer(payments, many=True)
        return Response(serializer.data)