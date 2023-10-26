import mimetypes

from django.shortcuts import get_object_or_404

from file_handler.celery import app
from files.models import File

from .services import Handlers


# TODO: написать обработчики файлов
@app.task
def files_handler(id: int) -> str:
    """
    - Берем файл по его id
    - Определяем его тип
    - Взависимости от типа файла, производим обработку
    - Если файл обработан успешно
      изменяем поле - processed, объекта(instance) файла на True
    """
    instance = get_object_or_404(File, id=id)

    file_name = instance.file.name
    file_extension = file_name.split('.')[-1]
    mime_type, encoding = mimetypes.guess_type(f'file.{file_extension}')
    mime_type = mime_type.split('/')[0]

    try:
        if mime_type == 'image':
            Handlers.image_handler(instance)
        if mime_type == 'text':
            Handlers.text_handler(instance)
        if mime_type == 'audio':
            Handlers.audio_handler(instance)
    except Exception as er:
        return f'Возникла ошибка при обработке файла {er}'

    instance.processed = True
    instance.save()
    return f'Обработка файла {file_name} успешно завершена'
