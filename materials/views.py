from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Course через Viewsets
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    """
    CRUD создание сущности для модели Lesson через Generic
    """
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """
    CRUD отображение списка сущностей для модели Lesson через Generic
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    CRUD отображение одной сущности для модели Lesson через Generic
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    CRUD редактирование сущности для модели Lesson через Generic
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    CRUD удаление сущности для модели Lesson через Generic
    """
    queryset = Lesson.objects.all()



