from rest_framework import serializers
from .models import Travel

from django.contrib.auth.models import User


# Hyperlinking the User model with the Travel model
class TravelSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Travel model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='travel-highlight',
                                                     format='html')


    class Meta:
        model = Travel  # Adjust the model path as necessary
        fields = '__all__'  # Include all fields from the model

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the User model.
    """
    travels = serializers.HyperlinkedRelatedField(many=True, view_name='travel-detail', read_only=True)

    class Meta:
        model = User  # Adjust the model path as necessary
        fields = ['id', 'username', 'travels']

        
# class UserSerializer(serializers.ModelSerializer):
#     travels = serializers.PrimaryKeyRelatedField(many=True, queryset=Travel.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'travels']
#
# class TravelSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the SnippetClass model.
#     """
#     owner = serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model = Travel  # Adjust the model path as necessary
#         fields = '__all__'  # Include all fields from the model
