from django.contrib import admin
from region.models import *


class InstanceInlineIndustry(admin.TabularInline):
    model = IndustryMetaModel


@admin.register(IndustryModel)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [InstanceInlineIndustry]


class InstanceInlineRegionCity(admin.TabularInline):
    model = RegionCityModel


class InstanceInlineRegionMeta(admin.TabularInline):
    model = RegionMetaModel


# @admin.register(RegionModel)
# class IndustryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
#     inlines = [InstanceInlineRegionCity, InstanceInlineRegionMeta]
#

@admin.register(StoriesModel)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
