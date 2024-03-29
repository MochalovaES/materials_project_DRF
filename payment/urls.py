from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentListAPIView

app_name = PaymentConfig.name


urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
]