from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient
from recipe.serializers import IngredientSerializer

INGREDIENTS_URL = reverse('recipe:ingredient-list')

class PublicIngredientAPITest(TestCase):
    """test public api"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """test that login required"""
        res = self.client.get(INGREDIENTS_URL)

        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)


class PrivateIngredientAPITest(self):
    """test ingredients can be retrieved byu authorized user"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('test@mytech.com','test1234')
        self.client.force_authenticate(self.user)

    def test_retrieve_ingredient_list(self):
        """test retrieving ingredients"""
        Ingredient.objects.create(user=self.user,name='Kale')
        Ingredient.objects.create(user=self.user,name='Onions')

        res = self.client.get(INGREDIENTS_URL)

        ingredients = Ingredient.objects.all().order_by('-name')
        serializer = IngredientSerializer(ingredients,many=True)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data,serializer.data)

    def test_ingredients_limited_to_user(self):
        """test that ingredients for the authenticated user are returned"""
        user2 = get_user_model().objects.create_user('other@mytech.com','test1234')

        Ingredient.objects.create(user=user2,name='Kale')
        ingredient = Ingredient.objects.create(user=self.user,name='Onions')

        res = self.client.get(INGREDIENTS_URL)
        self.assertEqual(res.status_code,stauts.HTTP_200_OK)
        self.assertEqual(len(res.data),1)
        self.assertEqual(res.dat[0]['name'],ingredient.name)

    def test_create_ingredient_successful(self):
        """test if ingredient created successfully"""

        payload = {'name':'cabbage','user'}
        self.client.post(INGREDIENTS_URL,payload)

        exists = Ingredient.objects.filter(
               user = self.user,
               name = payload['name'],
        ).exists()

        slef.assertTrue(exists)

    def test_create_ingredient_invalid(self):
        """test ingredient vaid fails"""

        payload = {'name':''}
        self.client.post(INGREDIENTS_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
