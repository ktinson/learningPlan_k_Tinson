from rest_framework import serializers
from .models import Card
class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id','name', 'description', 'large', 'image')