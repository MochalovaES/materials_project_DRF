from datetime import datetime, timedelta
from celery import shared_task
from users.models import User


@shared_task
def check_user_activity():
    """ Периодическая задача, которая проверяет пользователей по дате
        последнего входа и, если пользователь не заходил более месяца,
        блокировать его с помощью флага is_active
    """
    # Определение контрольной даты
    target_date = datetime.now() - timedelta(days=30)
    users = User.objects.all()
    for user in users:
        if user.last_login < target_date:
            user.is_active = False
            user.save()
            print('Пользователь заблокирован')
