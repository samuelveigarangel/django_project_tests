from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="samuel", email="samuel@email.com", password="admin"
        )
