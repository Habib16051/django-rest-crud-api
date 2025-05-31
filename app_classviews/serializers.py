from rest_framework import serializers
from .models import Travel
class TravelSerializer(serializers.ModelSerializer):
    """
    Serializer for the SnippetClass model.
    """
    class Meta:
        model = Travel  # Adjust the model path as necessary
        fields = '__all__'  # Include all fields from the model