from django.db import models
import uuid

# Create your models here.

class WeekDays(models.TextChoices):
    MONDAY = "Monday", "Lunes"
    TUESDAY = "Tuesday", "Martes"
    WEDNESDAY = "Wednesday", "Miércoles"
    THURSDAY = "Thursday", "Jueves"
    FRIDAY = "Friday", "Viernes"
    SATURDAY = "Saturday", "Sábado"
    SUNDAY = "Sunday", "Domingo"

class Entree(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class MainDish(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Dessert(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Menu(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    day_of_week = models.CharField(max_length=15, choices=WeekDays.choices)
    entree = models.ForeignKey(Entree, on_delete=models.CASCADE, related_name='menus')
    main_dish = models.ForeignKey(MainDish, on_delete=models.CASCADE, related_name='menus')
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE, related_name='menus')

    def __str__(self):
        return f"Entrada: {self.entree.name}, plato principal: {self.main_dish.name} y postre: {self.dessert.name}"

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    buyer = models.CharField(max_length=200, null=False)
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING, related_name='orders', null=False)