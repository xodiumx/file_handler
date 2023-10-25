from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from files.models import File

from .serializers import FileSerializer, UploadSerializer


class UploadViewSet(CreateModelMixin, GenericViewSet):
    
    http_method_names = ('post',)
    serializer_class = UploadSerializer

    
class FileViewSet(ListModelMixin, GenericViewSet):

    queryset = File.objects.all()
    http_method_names = ('get',)
    serializer_class = FileSerializer
