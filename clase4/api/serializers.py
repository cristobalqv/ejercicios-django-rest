from rest_framework import serializers
from api.models import Libro, Revista


#convierte los modelos en un formato enviable desde una API (Json... etc)

class LibroSerializer(serializers.ModelSerializer):    #ModelSerializer es una clase que simplifica creacion de serializadores
    class Meta:        #configuracion interna del serializer
        model=Libro
        fields='__all__'    #incluye todos los campos del modelo. Se pueden escoger menos campos para mostrar. Puede ser una lista también




class RevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Revista
        fields='__all__'

