from django.core.management import BaseCommand

from users.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        payment_list = [
            {'user_id': '1', 'date': '2024-02-15', 'course_id': '1', 'amount': '1500', 'method': 'Наличные'},
            {'user_id': '1', 'date': '2024-02-15', 'course_id': '2', 'amount': '2000', 'method': 'Перевод'},
            {'user_id': '1', 'date': '2024-02-15', 'lesson_id': '1', 'amount': '1500', 'method': 'Наличные'},
            {'user_id': '1', 'date': '2024-02-15', 'lesson_id': '2', 'amount': '2000', 'method': 'Перевод'},
        ]
        Payment.objects.all().delete()

        for payment in payment_list:
            Payment.objects.create(**payment)
