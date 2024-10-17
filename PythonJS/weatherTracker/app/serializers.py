from rest_framework import serializers
from .models import Profile, Search
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields ='__all__'
#