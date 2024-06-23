from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema


MESSAGE = 'Funcionando corretamente!'
DESCRIPTION = 'Endpoint de saúde da aplicação'
class HealthView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        operation_description=DESCRIPTION,
        operation_summary=DESCRIPTION,
        responses={200: MESSAGE}
    )
    def get(self, _):
        return Response(MESSAGE)