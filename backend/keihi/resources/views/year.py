from resources.serializers import YearSerializer
from resources.services import YearServices
from resources.utils.tags import RESOURCES_TAG
from resources.utils.views import YEAR_ALL_DESCRIPTION

from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema


class YearView(APIView):
    permission_classes = []
    
    @swagger_auto_schema(
        operation_summary=YEAR_ALL_DESCRIPTION,
        tags=[RESOURCES_TAG]
    )
    def get(self, _):
        payments = YearServices.get_all()
        serializer = YearSerializer(payments, many=True)
        return Response(serializer.data)