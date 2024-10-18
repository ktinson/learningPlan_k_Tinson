from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CardsSerializer
from .models import Card

# Create your views here.
class CardView(viewsets.ModelViewSet):
    serializer_class = CardsSerializer
    queryset = Card.objects.all()