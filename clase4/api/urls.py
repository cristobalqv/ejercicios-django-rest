from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()    #Automatiza la generación de rutas para las vistas registradas. Evita escribir manualmente cada endpoint
router.register(r'libros', views.LibroViewSet)   
router.register(r'revistas', views.RevistaViewSet)

'''libros es el prefijo URL usado para esta ruta. Puedo definir varias rutas segun cuantos endpoints queramos tener.       Usamos la r para forzar que esta ruta sea leida como URL completa    por ejemplo:  /libros/1  corresponde a un libro con pk 1, sin embargo   /libros/n  puede ser interpretado como un salto de linea, lo que generaria error'''


urlpatterns = [
    path('', include(router.urls)),
    # path('api/', include(router.urls))
]

