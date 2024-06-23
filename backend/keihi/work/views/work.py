from rest_framework.response import Response
from rest_framework.views import APIView
from work.models import Work

from drf_yasg.utils import swagger_auto_schema

class WorkView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        operation_summary="Retorna uma lista de trabalhos realizados",
    )
    def get(self, _):
        works = Work.objects.all()
        return Response(works)