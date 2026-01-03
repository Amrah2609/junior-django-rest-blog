from rest_framework import serializers
from favourite.models import Favourite

class FavouriteListCreateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

class FavouriteAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'
