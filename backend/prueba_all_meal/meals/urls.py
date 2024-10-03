from django.urls import path, include
from rest_framework.routers import DefaultRouter
from meals.views import MainDishList

router = DefaultRouter()
router.register(r'maindish', MainDishList)

urlpatterns = [
    path('', include(router.urls)),
]
