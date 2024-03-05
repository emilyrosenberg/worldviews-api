from .models import Location
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import LocationSerializer


class LocationList(generics.ListCreateAPIView):
    """
    Location
    """
    serializer_class = LocationSerializer
    queryset = Location.objects.annotate().order_by('name')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'name',
    ]
    ordering_fields = [
        'name',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
