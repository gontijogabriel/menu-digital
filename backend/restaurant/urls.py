from django.urls import path
from restaurant.views import RestaurantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurant', RestaurantViewSet, basename='restaurant')

urlpatterns = [
]
urlpatterns += router.urls
