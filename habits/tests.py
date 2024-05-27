from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from habits.models import Habit
from users.models import User


class AllTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.pro', is_active=True, is_superuser=True, is_staff=True)
        self.user.set_password('qqqwww111222')

        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        data = {"place": "место",
                "time": "18:00:00",
                "action": "действие",
                "sign_pl_habit": False,
                "periodicity": 7,
                "sign_publication": True
                }
        response = self.client.post(reverse('habits:habit-create'), data=data)
        print(response)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_habits(self):
        response = self.client.get(reverse('habits:habit-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        habit = Habit.objects.create(is_author=self.user,
                                     place="место",
                                     time="18:00:00",
                                     action="действие",
                                     sign_pl_habit=False,
                                     periodicity=7,
                                     sign_publication=True
                                     )
        update_data = {
            "place": "update",
        }

        response = self.client.patch(reverse('habits:habit-update', args=[habit.id]), update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_habit(self):
        habit = Habit.objects.create(is_author=self.user,
                                     place="место",
                                     time="18:00:00",
                                     action="действие",
                                     sign_pl_habit=False,
                                     periodicity=7,
                                     sign_publication=True
                                     )

        response = self.client.delete(reverse('habits:habit-delete', args=[habit.id]))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_author_habit(self):
        response = self.client.get(reverse('habits:habit-author-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
