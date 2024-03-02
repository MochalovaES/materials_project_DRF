from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.paginators import MaterialsPagination
from materials.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.services import get_url_payment
from payment.models import Payment
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Course через Viewsets
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MaterialsPagination

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'partial_update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAuthenticated, IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.user = self.request.user
        new_course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    """
    CRUD создание сущности для модели Lesson через Generic
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """
    CRUD отображение списка сущностей для модели Lesson через Generic
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    CRUD отображение одной сущности для модели Lesson через Generic
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    CRUD редактирование сущности для модели Lesson через Generic
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    CRUD удаление сущности для модели Lesson через Generic
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """
    CRUD создание сущности для установки подписки пользователя через Generic
    """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course_id')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user).filter(course=course_id).all()
        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subscription_id = subs_item[0].pk
            subscription = Subscription.objects.get(pk=subscription_id)
            subscription.delete()
            message = 'подписка удалена'
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            new_subscription = {
                "user": user,
                "course_id": course_id
            }
            Subscription.objects.create(**new_subscription)
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response({"message": message})


class CoursePaymentAPIView(APIView):
    """
    Создание сущности для возможности оплаты Курсов
    """

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data["course"]

        course_item = get_object_or_404(Course, pk=course_id)

        if course_item:
            url_for_payment = get_url_payment(course_item)
            message = 'Оплата курса'
            data = {
                "user": user,
                "date": '2024-02-27',
                "course": course_item,
                "amount": course_item.price,
                "method": 'Перевод',
                "url_for_payment": url_for_payment,
            }
            payment = Payment.objects.create(**data)
            payment.save()
            return Response({"message": message, "url": url_for_payment})
        else:
            message = 'Курс для оплаты не найден'
            return Response({"message": message})
