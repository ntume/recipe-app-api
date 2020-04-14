from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient
from recipe import serializers

class BaseRecipeAtrrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):

    """base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        """return objects of current authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self,serializer):
        """create a new object"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAtrrViewSet):
    """manage tags in db"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAtrrViewSet):

    """manage ingredients in the db"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer




"""
class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    "manage tags in db"
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_querset(self):
        "return objects for the current authenticated user only"
        return self.queryset.filter(user = self.request.user).order_by('-name')

    def perform_create(self,serializer):
        "create a new tag"
        serializer.save(user=self.request.user)


class IngredientViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):

    manage ingredients in the db
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

    def get_queryset(self):
        "return objects for surrent user"
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self,serializer):
        "create a new ingredient"
        serializer.save(user=self.request.user)
"""
