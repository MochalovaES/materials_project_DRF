from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    """
    Создание модели Курс
    """
    name = models.CharField(max_length=150, verbose_name='Наименование курса')
    image = models.ImageField(upload_to='materials/', verbose_name='изображение', **NULLABLE)
    description = models.CharField(max_length=500, verbose_name='Описание курса')
    amount = models.IntegerField(default=1000, verbose_name='цена')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return {self.name}

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """
    Создание модели Урок
    """
    name = models.CharField(max_length=150, verbose_name='Наименование урока')
    description = models.CharField(max_length=500, verbose_name='Описание урока')
    image = models.ImageField(upload_to='materials/', verbose_name='изображение', **NULLABLE)
    link_video = models.CharField(max_length=200, verbose_name='Ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс pk')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return {self.name}

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    """
    Создание модели Подписка
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


