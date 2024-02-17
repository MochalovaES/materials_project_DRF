from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'description', 'link_video']


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_count_lessons(self, instance):
        return len(Lesson.objects.all().filter(course=instance.pk))

    class Meta:
        model = Course
        fields = ['name', 'description']





