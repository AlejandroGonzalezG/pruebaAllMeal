from rest_framework import serializers
from meals.models import Dessert, Entree, MainDish, Menu, Order

class EntreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entree
        fields = '__all__'

class MainDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDish
        fields = '__all__'

class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
