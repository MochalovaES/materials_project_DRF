from rest_framework.test import APITestCase
from rest_framework import status
from materials.models import Course, Lesson, Subscription
from users.models import User


class CourseAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            email="test_mail@test.com",
            phone="12345",
            country="test_city",
            password='12345'
        )
        self.course = Course.objects.create(
            id=10,
            name="Course_test 1",
            description="Course_descroption 1",
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            id=1,
            name="Lesson_test 1",
            description="Lesson_discription 1",
            link_video="youtube.com",
            course=self.course,
            owner=self.user
        )

    def test_get_list_course(self):
        """ Тестирование отображения списка курсов """
        self.client.force_authenticate(user=self.user)
        responce = self.client.get(
            '/course/')
        self.assertEquals(
            responce.status_code,
            status.HTTP_200_OK
        )

    def test_create_course(self):
        """ Тестирование создания курса """
        data = {
            "name": "Course_test 2",
            "description": "Course_descroption 2",
            "owner": self.user
        }
        self.client.force_authenticate(user=self.user)
        responce = self.client.post(
            '/course/',
            data=data)

        self.assertEquals(
            responce.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_course(self):
        """ Тестирование удаления курса """
        self.client.force_authenticate(user=self.user)
        responce = self.client.delete(
            '/course/10/')

        self.assertEquals(
            responce.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_get_list_lesson(self):
        """ Тестирование отображения списка уроков """
        self.client.force_authenticate(user=self.user)
        responce = self.client.get(
            '/lesson/')
        self.assertEquals(
            responce.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        """ Тестирование создания урока """
        data = {
            "name": "LessonTest 2",
            "description": "Lesson_description 2",
            "owner": self.user,
            "link_video": "youtube.com",
        }
        print(data)
        self.client.force_authenticate(user=self.user)
        responce = self.client.post(
            '/course/',
            data=data)
        print(responce)
        self.assertEquals(
            responce.status_code,
            status.HTTP_201_CREATED
        )

    def test_delete_lesson(self):
        """ Тестирование удаления урока """
        self.client.force_authenticate(user=self.user)
        responce = self.client.delete(
            '/lesson/delete/1/')
        print(Lesson.objects.all())

        self.assertEquals(
            responce.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            id=1,
            email="test_mail@test.com",
            phone="12345",
            country="test_city",
            password='12345'
        )
        self.course = Course.objects.create(
            id=1,
            name="Course_test 1",
            description="Course_descroption 1",
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            id=1,
            name="Lesson_test 1",
            description="Lesson_discription 1",
            link_video="youtube.com",
            course=self.course,
            owner=self.user
        )
        self.subscription = Subscription.objects.create(
            course=self.course,
            user=self.user,
        )

    def test_create_subscription(self):
        """
        Тестирование создания подписки на курс
        """
        data = {
            "course_id": 1,
            "user": 1
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/subscription/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


