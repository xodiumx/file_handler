from django.contrib.admin import ModelAdmin, register

from .models import File


@register(File)
class FileAdmin(ModelAdmin):
    
    list_display = ('file', 'uploaded_at', 'processed')
    list_filter = ('file', 'uploaded_at', 'processed')
    search_fields = ('file', 'uploaded_at', )
    empty_value_display = '-пусто-'
    