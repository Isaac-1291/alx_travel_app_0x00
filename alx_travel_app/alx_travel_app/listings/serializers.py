"""
Serializers for the listings app.
"""
from rest_framework import serializers
from .models import Listing, ListingImage

class ListingImageSerializer(serializers.ModelSerializer):
    """
    Serializer for listing images.
    """
    class Meta:
        model = ListingImage
        fields = ['id', 'image', 'alt_text', 'is_primary', 'created_at']
        read_only_fields = ['id', 'created_at']

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for travel listings.
    """
    images = ListingImageSerializer(many=True, read_only=True)
    host_name = serializers.CharField(source='host.get_full_name', read_only=True)
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'property_type', 'price_per_night',
            'location', 'latitude', 'longitude', 'max_guests', 'bedrooms',
            'bathrooms', 'amenities', 'is_available', 'host', 'host_name',
            'images', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'host', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        """
        Create a new listing with the current user as host.
        """
        validated_data['host'] = self.context['request'].user
        return super().create(validated_data)
