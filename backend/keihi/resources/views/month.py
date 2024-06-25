from resources.serializers import MonthSerializer
from resources.services import MonthServices
from resources.utils.tags import RESOURCES_TAG
from resources.utils.views import MONTH_ALL_DESCRIPTION

from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

class MonthView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        operation_summary=MONTH_ALL_DESCRIPTION,
        tags=[RESOURCES_TAG]
    )
    def get(self, _):
        payments = MonthServices.get_all()
        serializer = MonthSerializer(payments, many=True)
        return Response(serializer.data)
    
