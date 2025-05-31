from rest_framework import serializers
from .models import Travel

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    travels = serializers.PrimaryKeyRelatedField(many=True, queryset=Travel.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'travels']

class TravelSerializer(serializers.ModelSerializer):
    """
    Serializer for the SnippetClass model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Travel  # Adjust the model path as necessary
        fields = '__all__'  # Include all fields from the model