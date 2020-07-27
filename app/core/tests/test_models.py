from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@EXAMPLE.COM'
        user = get_user_model().objects.create_user(email=email, password='Test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test the email for a new user is invalid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='Test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@example.com', password='Test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_superuser_email_normalized(self):
        """Test the email for a new superuser is normalized"""
        email = 'test@EXAMPLE.COM'
        user = get_user_model().objects.create_superuser(email=email, password='Test123')

        self.assertEqual(user.email, email.lower())

    def test_new_superuser_invalid_email(self):
        """Test the email for a new superuser is invalid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(email=None, password='Test123')
