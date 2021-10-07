# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.deletion import DO_NOTHING


# Create your models here.

class Diasdevoluntariado(models.Model):
    DIAS_SEMANA = (
        ('LUN', 'LUNES'),
        ('MAR', 'MARTES'),
        ('MIE', 'MIERCOLES'),
        ('JUE', 'JUEVES'),
        ('VIE', 'VIERNES'),
        ('SAB', 'SABADO'),
        ('DOM', 'DOMINGO'),
    )
    iddia = models.AutoField(db_column='IdDia', primary_key=True) 
    diaarealizar = models.CharField(
        'Día a Realizar', 
        db_column='DiaARealizar', 
        max_length=3, 
        choices=DIAS_SEMANA
        )
    horasaprox = models.CharField('Horas aprox', db_column='HorasAprox', max_length=10) 
    voluntario = models.ForeignKey(
        'voluntario.voluntario',
        related_name='dias_voluntario', 
        db_column='FKIdVoluntario',
        on_delete=DO_NOTHING
        )


    def __str__(self):
        return '%s' % (self.voluntario)

    class Meta:
        verbose_name = 'Día de Voluntariado'
        verbose_name_plural = 'Días de Voluntariado'
        managed = False
        db_table = 'diasdevoluntariado'