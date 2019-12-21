from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from . import serializers
from projects import models as p_models
from setups import models as s_models


class ProjectList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['projects']
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        region_id = self.kwargs['region_id']
        return p_models.Project.objects.filter(region_id=region_id)


class RegionList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['projects']
    queryset = s_models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
