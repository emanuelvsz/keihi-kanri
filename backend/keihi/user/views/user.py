from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    permission_classes = []

    def get(self, _):
        return Response("Funcionando corretamente!")