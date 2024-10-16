from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, SearchSerializer
from .models import User, Search
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserView(generics.CreateAPIView):
    queryset = User.objects.all
    serializer_class = UserSerializer
    
class SearchView(generics.CreateAPIView):
    queryset = Search.objects.all
    serializer_class = SearchSerializer
#     form = UserCreationForm()
#     return render(request, "api,register.html", {"form": form})