from datetime import datetime

from django.db import models


class File(models.Model):
    """
    """
    file = models.FileField(
        'Файл',
        null=False,
        blank=False,
        upload_to='files/'
    )
    uploaded_at = models.DateTimeField(
        'Дата загрузки',
        null=False,
        default=datetime.now,
    )
    processed = models.BooleanField(
        'Обработан',
        null=False,
        default=False,
    )

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ('uploaded_at',)
