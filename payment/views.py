from rest_framework import generics
from rest_framework.filters import OrderingFilter

from users.serializers import PaymentSerializer
from models import Payment
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class PaymentListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ('course', 'lesson', 'method')
    ordering_fields = ('date',)









