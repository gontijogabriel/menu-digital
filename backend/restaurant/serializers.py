from rest_framework import serializers
from restaurant.models import Restaurant
import re

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data['cnpj'] = re.sub(r'\D', '', validated_data['cnpj'])
        return super(RestaurantSerializer, self).create(validated_data)