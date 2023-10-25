from collections import OrderedDict

from rest_framework.serializers import ModelSerializer

from files.models import File


class FileSerializer(ModelSerializer):
    
    class Meta:
        model = File
        fields = ('file', 'uploaded_at', 'processed')



class UploadSerializer(ModelSerializer):
    
    class Meta:
        model = File
        fields = ('file', )
