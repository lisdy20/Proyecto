# -*- coding: utf-8 -*-
from django.db import models
from caravanamigrante.models import Caravanamigrante
from authuser.models import AuthUser

# Create your models here.

class Migrante(models.Model):

    GENERO_CHOICE = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OTRO'),
    )


    idmigrante = models.AutoField(db_column='IdMigrante', primary_key=True) 
    nombre = models.CharField('Nombre:', db_column='Nombre', max_length=50) 
    apellido = models.CharField('Apellido:', db_column='Apellido', max_length=50) 
    telefono = models.CharField('Teléfono:', db_column='Telefono', max_length=16) 
    genero = models.CharField('Género:', db_column='Genero', choices=GENERO_CHOICE, max_length=1)
    edad = models.IntegerField('Edad:', db_column='Edad') 
    fechanacimiento = models.DateField('Fecha de Nacimiento:', db_column='FechaNacimiento')
    nacionalidad = models.CharField('Nacionalidad:', db_column='Nacionalidad', max_length=50)
    caravana = models.ForeignKey(Caravanamigrante, models.DO_NOTHING, db_column='FkIdCaravana') 
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='FKIdUsuario')


    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

    class Meta:
        verbose_name = 'Migrante'
        verbose_name_plural = 'Migrantes'
        managed = False
        db_table = 'migrante'