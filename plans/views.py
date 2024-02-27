# from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Plan
from .serializers import PlanSerializer


class PlanList(generics.ListCreateAPIView):
    """
    List plan or create a plan if logged in
    The perform_create method associates the plan with the logged in user.
    """
    serializer_class = PlanSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Plan.objects.annotate(
        # likes_count=Count('likes', distinct=True),
        # comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'owner__username',
        'title',
    ]
    # ordering_fields = [
    #     'comments_count',
    # ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlanDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a plan and edit or delete it if you own it.
    """
    serializer_class = PlanSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Plan.objects.annotate(
        # likes_count=Count('likes', distinct=True),
        # comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
