from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from Gentera.api import urls as urlsAPI

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^API/', include(urlsAPI, namespace='APIs'))
]
