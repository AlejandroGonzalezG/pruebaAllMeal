from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from meals.models import Dessert, Entree, MainDish, Menu
from meals.serializers import DessertSerializer, EntreeSerializer, MainDishSerializer, MenuSerializer

class MainDishList(ListModelMixin, GenericAPIView):
    queryset = MainDish.objects.all()
    serializer_class = MainDishSerializer

    def get(self, request):
        return Response({"message": "Hello from Django!"})