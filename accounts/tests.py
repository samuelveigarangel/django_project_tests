from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="samuel", email="samuel@email.com", password="admin"
        )
        self.assertEqual(user.username, "samuel")
        self.assertEqual(user.email, "samuel@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="samueladmin", email="samueladmin@email.com", password="admin"
        )
        self.assertEqual(admin_user.username, "samueladmin")
        self.assertEqual(admin_user.email, "samueladmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
