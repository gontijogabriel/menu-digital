from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from restaurant.serializers import RestaurantSerializer
from restaurant.models import Restaurant
import re


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer