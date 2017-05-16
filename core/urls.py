from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from core.views import ItemViewSet


router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

