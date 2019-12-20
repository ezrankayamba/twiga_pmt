from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from . import serializers
from projects import models as p_models


class ProjectList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['projects']
    queryset = p_models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
