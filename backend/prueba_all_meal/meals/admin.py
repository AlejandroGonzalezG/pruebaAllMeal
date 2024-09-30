from django.contrib import admin
from meals.models import Dessert, MainDish, Entree, Menu

# Register your models here.

admin.site.register(Dessert, admin.ModelAdmin)
admin.site.register(MainDish, admin.ModelAdmin)
admin.site.register(Entree, admin.ModelAdmin)
admin.site.register(Menu, admin.ModelAdmin)