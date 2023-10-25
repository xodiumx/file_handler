from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UploadViewSet, FileViewSet

router_v1 = DefaultRouter()
router_v1.register('upload', UploadViewSet, basename='upload')
router_v1.register('files', FileViewSet, basename='files')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
