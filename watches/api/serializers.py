from rest_framework import serializers

from ..models import Watch


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = ('brand', 'model', 'describtion', 'price', 'discount_price')



class WatchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        # fields = '__all__'
        exclude = ("categories",)



class WatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = '__all__'



class WatchUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        # fields = '__all__'
        exclude = ("categories",)
