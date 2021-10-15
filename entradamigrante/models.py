# -*- coding: utf-8 -*-
from django.db import models
from migrante.models import Migrante
from django.core.exceptions import ValidationError


# Create your models here.

class Entradamigrante(models.Model):
    idmovilidad = models.AutoField(db_column='IdMovilidad', primary_key=True) 
    #salida = models.BooleanField("Salida" , default=False)
    migrante = models.ForeignKey(Migrante, models.DO_NOTHING, db_column='FkIdMigrante') 
    fechaentrada = models.DateTimeField('Fecha de Entrada', db_column='FechaEntrada', auto_now_add=True)
    checkout = models.BooleanField('Ha marcado salida?', default=False)
    módulo = models.ForeignKey(
        'modulo.modulo',
        related_name='modulo', 
        db_column='FkIdModulo',
        on_delete= models.DO_NOTHING,
        )
    descripcion = models.CharField('Descripción', db_column='Descripcion', max_length=254, blank=True,
        null=True) 

    def __str__(self):
        return '%s %s' % (self.migrante, self.módulo)

    def clean(self): 
        print(self.módulo.disponibilidad())
        if self.módulo.disponibilidad() == 0:
            raise ValidationError("No se puede ingresar al migrante al modulo {} debido a que se encuentra lleno.".format(self.módulo.nombre))


    class Meta:
        verbose_name = 'Entrada Migrante'
        verbose_name_plural = 'Entrada Migrantes'