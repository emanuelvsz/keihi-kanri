from rest_framework.response import Response
from rest_framework.views import APIView
from payment.models import Payment

from drf_yasg.utils import swagger_auto_schema

class PaymentView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        operation_summary="Retorna uma lista de pagamentos realizados",
    )
    def get(self, _):
        payments = Payment.objects.all()
        return Response(payments)