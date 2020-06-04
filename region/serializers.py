from rest_framework import serializers
from region.models import *


class IndustryMetaSerializer(serializers.ModelSerializer):
    """Общая информация по отросли в ЦФО"""

    class Meta:
        model = IndustryMetaModel
        fields = ('name', 'maps', 'value_one', 'value_two', 'value_three', 'value_four',)


class IndustrySerializer(serializers.ModelSerializer):
    """Отросли"""

    class Meta:
        model = IndustryModel
        fields = ('id', 'name', 'value_one', 'value_two', 'value_three', 'value_four')


class RegionSerializer(serializers.ModelSerializer):
    """Регионы"""

    class Meta:
        model = RegionModel
        fields = ('name', 'region_code',)


class RegionMetaSerializer(serializers.ModelSerializer):
    """Подробная информация по региону"""

    class Meta:
        model = RegionMetaModel
        fields = ('name',)


class RegionCitySerializer(serializers.ModelSerializer):
    """Крупные города и населенные пункты в регионе"""

    class Meta:
        model = RegionCityModel
        fields = ('name',)


class StoriesSerializer(serializers.ModelSerializer):
    """Истории успехов"""

    class Meta:
        model = StoriesModel
        fields = ('name', 'value_one', 'value_two', 'value_three', 'value_four')
