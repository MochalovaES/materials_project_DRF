from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Course через Viewsets
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

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


