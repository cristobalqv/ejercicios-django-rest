from django.db import models

# Create your models here.

class Libro(models.Model):

    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    num_paginas = models.IntegerField()

    def __str__(self):
        return self.titulo
    


FRECUENCIA = [('DIARIA', 'Diaria'),         #(a,b)   a mostrado en base de datos,    b al usuario
              ('SEMANAL', 'Semanal'),
              ('MENSUAL', 'Mensual')]

class Revista(models.Model):

    titulo = models.CharField(max_length=100)
    tema = models.CharField(max_length=50)
    frecuencia_publicacion = models.CharField(max_length=20, choices=FRECUENCIA)
    num_edicion = models.IntegerField()

    def __str__(self):
        return self.titulo
    

