from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Watch
from .serializers import (
    WatchCreateSerializer,
    WatchListSerializer,
    WatchDetailSerializer,
    WatchUpdateSerializer
)


# Function base views (api)

@api_view(['GET'])
def all_watches(request):
    watches = Watch.objects.all()
    serializer = WatchListSerializer(watches, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
def create_watch(request):
    serializer = WatchCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(seller=request.user)
        return Response({'detail': 'Watch yaradıldı'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detail_watch(request, pk):
    watch = get_object_or_404(Watch, pk=pk)
    if request.method=='GET':
        serializer = WatchDetailSerializer(watch)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'detail': 'Sorğu növü düzgün deyil.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PATCH'])
def update_watch(request, pk):
    watch = get_object_or_404(Watch, pk=pk)
    if request.method=='PATCH':
        serializer = WatchUpdateSerializer(data=request.data, instance=watch, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Məlumatlar yeniləndi'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail': 'Sorğu növü düzgün deyil.'}, status=status.HTTP_4c05_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_watch(request, pk):
    watch = get_object_or_404(Watch, pk=pk)
    if request.method=='DELETE':
        watch_id = watch.id
        watch.delete()
        return Response({'detail': f'{watch_id} id-li watch silindi.'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'detail': 'Sorğu növü düzgün deyil.'}, status=status.HTTP_4c05_METHOD_NOT_ALLOWED)
    