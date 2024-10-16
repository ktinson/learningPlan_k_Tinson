from rest_framework import serializers
from .models import UserProfile, Search
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'password', 'email')
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('id', 'searchTerm')