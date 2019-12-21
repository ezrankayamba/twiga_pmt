from django.shortcuts import render
from projects import models as p_models
from setups import models as s_models
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = p_models.Project
        fields = ('id', 'name', "region", "latitude", "longitude")


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = s_models.Region
        fields = ('id', 'name')
