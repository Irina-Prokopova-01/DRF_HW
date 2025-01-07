from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from Ims.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()

        self.user = User.objects.create(email="irina@yandex.ru", password="12345")
        self.course = Course.objects.create(title="Программирование")
        self.lesson = Lesson.objects.create(
            title="Python",
            video="https://irina.youtube.com/",
            course=self.course,
            owner=self.user,
        )

        self.client.force_authenticate(user=self.user)

    def test_getting_lesson_list(self):
        """Тестирование получения списка уроков."""
        response = self.client.get("/lesson/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json()["results"],
            [
                {
                    "id": 3,
                    "course": None,
                    "title": "Python",
                    "description": "",
                    "preview": None,
                    "video": "http://irina@youtube.com",
                    "owner": 1,
                }
            ],
        )

    def test_lesson_create(self):
        """Тестируем создание урока"""
        url = reverse("Ims:lesson-create")
        data = {
            "title": "C++",
            "course": self.course.pk,
            "video": "https://youtube.com/",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
            {
                "id": 3,
                "title": "C++",
                "picture": None,
                "description": None,
                "video": "https://youtube.com/",
                "course": 2,
                "owner": 2,
            },
        )

    def test_lesson_update(self):
        """Тестируем изменение урока"""
        url = reverse("Ims:lesson-update", args=(self.lesson.pk,))
        data = {"title": "Python", "video": "https://test.youtube.com/"}

        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()["title"], "test_lesson_2")

    def test_lesson_detail(self):
        """Тестируем изменение урока"""
        url = reverse("Ims:lesson-detail", args=(self.lesson.pk,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()["title"], "test_lesson")

    def test_lesson_delete(self):
        """Тестируем изменение урока"""
        url = reverse("Ims:lesson-delete", args=(self.lesson.pk,))

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    """Тест подписки на курс."""

    def setUp(self):
        self.user = User.objects.create(email="test@yandex.ru")
        self.course = Course.objects.create(title="Программирование", owner=self.user)
        self.new_course = Course.objects.create(title="New", owner=self.user)
        self.subscription = Subscription.objects.create(
            user=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription_delete(self):
        """Тест создания/отмены подписки."""
        data = {"pk": self.course.id}
        url = reverse("Ims:subscription")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Подписка была удалена.")

    def test_subscription_create(self):
        """Тест создания/отмены подписки."""
        data = {"pk": self.new_course.id}
        url = reverse("Ims:subscription")
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Подписка была создана.")
