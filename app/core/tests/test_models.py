from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """
    docstring
    """

    def test_create_user_with_email_successful(self):
        """
        Test creating a user with email address is successful
        """
        email = 'vkathirvel+test@gmail.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'vkathirvel+test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'TestPass123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'TestPass123')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'vkathirvel+test@gmail.com',
            'TestPass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
