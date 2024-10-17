from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from app.serializers import ProfileSerializer, SearchSerializer
from .models import Profile, Search
# Create your views here.
def testingView(request):
    return HttpResponse("Testing")
class ProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
class SearchView(generics.CreateAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    