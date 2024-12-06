from django.contrib import admin
from api.models import Libro, Revista


# Register your models here. Para que admin tenga acceso

admin.site.register(Libro)
admin.site.register(Revista)

