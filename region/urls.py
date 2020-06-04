from django.urls import path
from region.views import *

urlpatterns = [
    path('industry/', IndustrySerializerView.as_view()),
    path('industryen/', IndustryEnSerializerView.as_view()),
    path('industry/<int:pk>/', IndustryMetaSerializerView.as_view()),
    path('region/', RigionSerializerView.as_view()),
    path('region/<int:pk>/', RegionMetaSerializerView.as_view()),
    path('projects/<int:pk>/', StoriesSerializerView.as_view()),
    path('cfo/', CFOSerializerView.as_view()),

]
