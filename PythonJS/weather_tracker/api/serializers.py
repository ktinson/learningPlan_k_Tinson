from rest_framework import serializers
from .models import User, Search
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('id', 'searchTerm')