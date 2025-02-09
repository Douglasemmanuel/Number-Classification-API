from rest_framework import serializers
from .models import NumberProperties

class NumberPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberProperties
        fields = ['number', 'is_perfect', 'is_prime', 'properties', 'digital_sum', 'fun_fact']
