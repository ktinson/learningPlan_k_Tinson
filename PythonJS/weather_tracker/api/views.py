from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User, Search
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserView(generics.CreateAPIView):
    queryset = User.objects.all
    serializer_class = UserSerializer
#     form = UserCreationForm()
#     return render(request, "api,register.html", {"form": form})