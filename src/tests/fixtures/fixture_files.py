import pytest

from rest_framework.test import APIClient

from files.models import File


@pytest.fixture
def user_client() -> APIClient:
    client = APIClient()
    return client


@pytest.fixture
def file() -> File:
    return File.objects.create(
        file = 'text.txt'
    )
