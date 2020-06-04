from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from region.serializers import *
from region.models import *


class IndustrySerializerView(ListAPIView):
    """Вывод всех отрослей на русском"""

    queryset = IndustryModel.objects.filter(slug='ru')
    serializer_class = IndustrySerializer


class IndustryEnSerializerView(ListAPIView):
    """Вывод всех отрослей на английском"""

    queryset = IndustryModel.objects.filter(slug='en')
    serializer_class = IndustrySerializer


class IndustryMetaSerializerView(APIView):
    """Вывод сведений об отдельной отросли"""

    def get(self, request, pk):
        industry = IndustryMetaModel.objects.filter(parent_id=pk)
        serializer = IndustryMetaSerializer(industry, many=True)
        return Response(serializer.data)


class RigionSerializerView(ListAPIView):
    """Вывод всех регионов"""

    queryset = RegionModel.objects.all()
    serializer_class = RegionSerializer


class RegionMetaSerializerView(APIView):
    """Вывод сведений об отдельном регионе"""

    def get(self, request, pk):
        meta = RegionMetaModel.objects.filter(parent__region_code=pk)
        city = RegionCityModel.objects.filter(parent__region_code=pk)
        serializer_meta = RegionMetaSerializer(meta, many=True)
        serializer_city = RegionCitySerializer(city, many=True)
        return Response({'meta': serializer_meta.data, 'city': serializer_city.data})


class StoriesSerializerView(APIView):
    """Вывод проектов"""

    def get(self, request, pk):
        projects = StoriesModel.objects.filter(parent_id=pk)
        indusrty = IndustryModel.objects.get(id=pk)
        name = indusrty.name
        serializer_project = StoriesSerializer(projects, many=True)
        return Response({'industry_name': name, 'serializer_project': serializer_project.data})


class CFOSerializerView(APIView):
    """Вывод общей информации по ЦФО"""

    def get(self, request):
        cfo = IndustryModel.objects.get(name='Общая статистика ЦФО')
        cfometa = IndustryMetaModel.objects.filter(parent_id=cfo.pk)
        serializer = IndustryMetaSerializer(cfometa, many=True)
        return Response(serializer.data)
