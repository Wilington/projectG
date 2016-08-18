from django.conf.urls import url
from . import views
from .views import UserListView, ContactoListView, LlamadaListView, AplicacionListView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^usuario/$', views.UserListView.as_view()),
    url(r'^contacto/$', views.ContactoListView.as_view()),
    url(r'^llamada/$', views.LlamadaListView.as_view()),
    url(r'^aplicacion/$', views.AplicacionListView.as_view()),
    ]
