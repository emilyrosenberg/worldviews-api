from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Plan
from .serializers import PlanSerializer


class PlanList(APIView):
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
