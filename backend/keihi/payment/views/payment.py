from rest_framework.response import Response
from rest_framework.views import APIView
from payment.models import Payment
from payment.serializers import PaymentSerializer
from payment.services import PaymentServices
from payment.serializers import PaymentCreateSerializer, PaymentUpdateSerializer, PaymentCompleteSerializer
from rest_framework import status
from keihi.serializers import GenericIDSerializer 

from drf_yasg.utils import swagger_auto_schema


class PaymentView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        operation_summary="Retorna uma lista de pagamentos realizados",
    )
    def get(self, _):
        payments = PaymentServices.get_all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Cria um pagamento",
        request_body=PaymentCreateSerializer, 
    )
    def post(self, request):
        serializer = PaymentCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        payment = PaymentServices.create(serializer.validated_data)
        return Response({"id": str(payment)}, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(
        operation_summary="Atualiza um pagamento",
        request_body=PaymentUpdateSerializer, 
    )
    def put(self, request):
        serializer = PaymentUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        payment = PaymentServices.update(serializer.validated_data)
        return Response({"id": str(payment)}, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(
        operation_summary="Completa um pagamento",
        request_body=PaymentCompleteSerializer, 
    )
    def patch(self, request):
        serializer = PaymentCompleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        payment = PaymentServices.complete_payment(
            serializer.validated_data
        )
        return Response({"id": str(payment)}, status=status.HTTP_204_NO_CONTENT)
    
    @swagger_auto_schema(
        operation_summary="Deleta um pagamento",
        request_body=GenericIDSerializer, 
    )
    def delete(self, request):
        serializer = GenericIDSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        PaymentServices.delete(
            serializer.validated_data.get('id', None)
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PaymentByMonthView(APIView):
    permission_classes = []
    
    @swagger_auto_schema(
        operation_summary="Retorna uma lista de pagamentos de um mês",
    )
    def get(self, _, month_id):
        payments = PaymentServices.get_payment_by_month(month_id)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
