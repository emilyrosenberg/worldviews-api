from dj_rest_auth.serializers import LocationSerializer
from rest_framework import serializers
from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    location = serializers.ReadOnlyField(source="location.name")

    class Meta(LocationSerializer.Meta):
        model = Location
        fields = ['location',]
