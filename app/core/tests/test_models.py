from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test@mytech.com',password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email,password)

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


    def test_tag_str(self):
        """test the tag string representation"""
        tag = models.Tag.objects.create(
            user = sample_user(),
            name = 'Vegan'
        )

        self.assertEqual(str(tag),tag.name)


    def test_ingredients_str(self):
        """test the ingredients string representation"""
        ingredient = models.Ingredient.objets.create(
                 user = sample_user(),
                 name = 'Cucumber'
        )

        self.assertEqual(str(ingredient),ingredient.name)
