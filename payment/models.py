from django.db import models

from materials.models import NULLABLE, Course, Lesson
from users.models import User


class Payment(models.Model):
    """
    Модель оплаты
    """
    METHOD_CHOICES = [
        ('Наличные', 'Наличные'),
        ('Перевод', 'Перевод'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateField(verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Курс')
    lesson = models.ForeignKey(Lesson, **NULLABLE, on_delete=models.SET_NULL, verbose_name='Урок')
    amount = models.PositiveIntegerField(verbose_name='Сумма')
    method = models.CharField(max_length=50, choices=METHOD_CHOICES, help_text='Выберите способ оплаты')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.course}:{self.lesson}  оплаченно на сумму {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


