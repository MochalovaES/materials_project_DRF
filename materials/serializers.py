from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import URLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'description', 'link_video']
        validators = [URLValidator(field='link_video')]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)
    course_subscription = serializers.SerializerMethodField()

    def get_count_lessons(self, instance):
        return len(Lesson.objects.all().filter(course=instance.pk))

    def get_course_subscription(self, instance):
        subscription = Subscription.objects.all().filter(course=instance.pk).filter(
            user=self.context.get('request').user.pk)
        if subscription:
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = ["id", "name", "description", "count_lessons", "lessons", "course_subscription"]


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'





