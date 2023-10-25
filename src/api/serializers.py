from collections import OrderedDict

from rest_framework.serializers import ModelSerializer

from files.models import File

from .tasks import files_handler


class FileSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = ('file', 'uploaded_at', 'processed')


class UploadSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = ('file', )

    def to_representation(self, instance: File) -> OrderedDict:
        """
        После создания объекта файла, отправляем его id
        в обработку celery task.
        """
        files_handler.delay(instance.id)
        return super().to_representation(instance)
