from rest_framework import serializers

from ..models import Watch


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = ('brand', 'model', 'describtion', 'price', 'discount_price')
