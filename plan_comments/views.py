from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import PlanComment
from .serializers import PlanCommentSerializer, PlanCommentDetailSerializer


class PlanCommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """

    serializer_class = PlanCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PlanComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["plan"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlanCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PlanCommentDetailSerializer
    queryset = PlanComment.objects.all()
