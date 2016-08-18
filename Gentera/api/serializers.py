from rest_framework import serializers
from ..models import Tm_User, Td_User_Cont, Td_User_Llam, Td_User_Apli

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tm_User
        fields = '__all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Td_User_Cont
        fields = '__all__'

class LlamadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Td_User_Llam
        fields = '__all__'

class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Td_User_Apli
        fields = '__all__'
