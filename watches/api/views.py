from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Watch
from .serializers import WatchListSerializer


# Function base views (api)

@api_view(['GET'])
def all_watches(request):
    watches = Watch.objects.all()
    serializer = WatchListSerializer(watches, many=True)
    return Response(serializer.data, status.HTTP_200_OK)
