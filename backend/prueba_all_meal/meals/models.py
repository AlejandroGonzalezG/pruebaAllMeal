from django.db import models

# Create your models here.

class Entree(models.Model):
    name = models.CharField(max_length=200)

class MainDish(models.Model):
    name = models.CharField(max_length=200)

class Dessert(models.Model):
    name = models.CharField(max_length=200)

class Menu(models.Model):
    entree = models.ForeignKey(Entree, on_delete=models.CASCADE, related_name='menus')
    main_dish = models.ForeignKey(MainDish, on_delete=models.CASCADE, related_name='menus')
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE, related_name='menus')

    def __str__(self):
        return f"Entrada: {self.entree.name}, plato principal: {self.main_dish.name} y postre: {self.dessert.name}"
