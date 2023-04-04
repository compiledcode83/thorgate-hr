from django.conf.urls import url, include

from rest_framework import routers

from projects.rest.views import ProjectViewSet


router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
]
