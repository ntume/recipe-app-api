from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""

        email = 'test@mytech.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(email = email, password = password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """test email for new user normalized (all small laters)"""
        email = 'test@MYTECH.com'
        user = get_user_model().objects.create_user(email = email,password='123455')
        self.assertEqual(user.email,email.lower())

        return user


    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,password='1234')


    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@mytech.com','1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
