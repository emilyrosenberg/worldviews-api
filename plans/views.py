# from django.db.models import Count
from rest_framework import generics, status, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Plan
from .serializers import PlanSerializer


class PlanList(APIView):
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

    def get(self, request):
        plans = Plan.objects.all()
        serializer = PlanSerializer(
            plans,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


def plan(self, request):
    serializer = PlanSerializer(
        data=request.data, context={'request': request}
    )
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED
        )

    return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )


class PlanDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PlanSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Plan.objects.annotate(
        # likes_count=Count('likes', distinct=True),
        # comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
