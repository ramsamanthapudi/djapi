from rest_framework import serializers
from .models import Products


class productserializer(serializers.ModelSerializer):
    access = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Products
        fields = '__all__'
