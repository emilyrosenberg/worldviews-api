from rest_framework import serializers
from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    location_id = serializers.ReadOnlyField(source="id")

    class Meta:
        model = Location
        fields = ['location_id', 'name']
