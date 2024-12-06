# from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import LibroSerializer, RevistaSerializer
from api.models import Libro, Revista


# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):    #ModelViewSet simplifica creación de vistas CRUD
    queryset = Libro.objects.all()            #Consulta a base de datos. Define los datos que se manejaran en los endpoints
    serializer_class=LibroSerializer          #conecta la vista con el serializer para transformar los datos correctamente a JSON u otro




class RevistaViewSet(viewsets.ModelViewSet):
    queryset = Revista.objects.all()
    serializer_class=RevistaSerializer