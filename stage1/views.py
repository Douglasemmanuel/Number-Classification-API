from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NumberPropertiesSerializer
from .models import NumberProperties
import requests

class NumberPropertiesView(APIView):
    def get(self, request, number):
        try:
            properties = self.get_properties(number)
            serializer = NumberPropertiesSerializer(properties)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"number":"alphabet","error":True}, status=status.HTTP_400_BAD_REQUEST)

    def get_properties(self, number):
        is_perfect = self.is_perfect_number(number)
        is_prime = self.is_prime_number(number)
        properties = self.get_properties_list(number)
        digital_sum = self.get_digital_sum(number)
        fun_fact = self.get_fun_fact(number)
        properties_obj = NumberProperties(
            number=number,
            is_perfect=is_perfect,
            is_prime=is_prime,
            properties=properties,
            digital_sum=digital_sum,
            fun_fact=fun_fact
        )
        return properties_obj

    def is_perfect_number(self, number):
        sum = 0
        for i in range(1, number):
            if number % i == 0:
                sum += i
        return sum == number

    def is_prime_number(self, number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def get_properties_list(self, number):
        properties = []
        if number % 2 == 0:
            properties.append('Even')
        else:
            properties.append('Odd')
        if number % 3 == 0:
            properties.append('Multiple of 3')
        return ', '.join(properties)

    def get_digital_sum(self, number):
        return sum(int(digit) for digit in str(number))

    def get_fun_fact(self, number):
        response = requests.get(f'http://numbersapi.com/{number}?json')
        return response.json()['text']