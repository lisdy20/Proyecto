# -*- coding: utf-8 -*-
from django.db import models
from authuser.models import AuthUser

# Create your models here.

class Donacion(models.Model):
    iddonacion = models.AutoField(db_column='IdDonacion', primary_key=True)
    nombre = models.CharField('Nombre o Entidad', db_column='Nombre', max_length=200)
    telefono = models.CharField('Teléfono', db_column='Telefono', max_length=18) 
    direccion = models.CharField('Dirección', db_column='Direccion', max_length=254)  
    descripcion = models.CharField('Descripción', db_column='Descripcion', max_length=254, blank=True,
        null=True)  
    fechadeentrega = models.DateTimeField('Entrega', db_column='FechaDeEntrega')
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='FKIdUsuario')


    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name = 'Donación'
        verbose_name_plural = 'Donaciones'