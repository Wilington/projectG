from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Tm_User, Td_User_Cont, Td_User_Llam, Td_User_Apli
from .serializers import UserSerializer, ContactoSerializer, LlamadaSerializer, AplicacionSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = Tm_User.objects.all()
    serializer_class = UserSerializer

class ContactoListView(generics.ListCreateAPIView):
    queryset = Td_User_Cont.objects.all()
    serializer_class = ContactoSerializer

class LlamadaListView(generics.ListCreateAPIView):
    queryset = Td_User_Llam.objects.all()
    serializer_class = LlamadaSerializer

class AplicacionListView(generics.ListCreateAPIView):
    queryset = Td_User_Apli.objects.all()
    serializer_class = AplicacionSerializer
