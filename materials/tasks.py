from datetime import datetime, timedelta, date
import pytz
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription, Course
from users.models import User


@shared_task
def send_mail_course_update(course_pk):
    """
    Отправка email сообщений пользователям об обновлении курса
    """
    users = [sub.user for sub in Subscription.objects.filter(course=course_pk, is_active=True)]
    course = Course.objects.get(pk=course_pk)
    send_mail(
        subject=f'Обновление курса {course.name}',
        message=f'Курс {course.name} обновлён',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email for user in users]
    )
    print("Отправлено")


@shared_task
def check_user_activity():
    """ Периодическая задача, которая проверяет пользователей по дате
        последнего входа и, если пользователь не заходил более месяца,
        блокировать его с помощью флага is_active
    """
    month = timedelta(days=31)
    # Определение контрольной даты
    key_date = date.today() - month

    for user in User.objects.filter(is_active=True, last_login__lt=key_date):
        user.is_active = False
        user.save(update_fields=["is_active"])
        print('Пользователь заблокирован')

