import pytest
from collections import OrderedDict

from http import HTTPStatus

from django.test.client import Client

from files.models import File


@pytest.mark.django_db(transaction=True)
class TestFile:
    files = '/api/v1/files/'
    upload = '/api/v1/upload/'

    def test_00_files(self, client: Client, file: File) -> None:
        response = client.get(self.files)
        data = response.data
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.files}` не найден.'
        )
        assert isinstance(data, list), (
            f'В ответе {data} - type - {type(data)} ожидается list'
        )
        assert isinstance(data[0], OrderedDict), (
            f'В ответе {data[0]} - type - {type(data[0])} - '
            'ожидается OrderedDict'
        )
        assert 'file' in data[0], (
            f'В {data[0]} отсутствует поле "file"'
        )
        assert 'uploaded_at' in data[0], (
            f'В {data[0]} отсутствует поле "uploaded_at"'
        )
        assert 'processed' in data[0],(
            f'В {data[0]} отсутствует поле "processed"'
        )
    
    def test_01_upload(self, client: Client, file: File) -> None:
        response = client.get(f'{self.upload}')
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            f'Эндпоинт `{self.upload}` должен поддерживать только post method'
        )
        response = client.post(f'{self.upload}')
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Эндпоинт `{self.upload}` не найден'
        )
