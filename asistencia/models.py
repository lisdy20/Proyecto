#From django libs and models
from django.db import models
from django.db.models.deletion import DO_NOTHING


class Asistencia(models.Model):
    idasistencia = models.AutoField(db_column='IdAsistencia', primary_key=True)  # Field name made lowercase.
    voluntario = models.ForeignKey(
        'voluntario.voluntario',
        related_name='voluntarios', 
        db_column='FKIdVoluntario',
        on_delete=DO_NOTHING
        )  # Field name made lowercase.
    entrada = models.TimeField('Entrada', db_column='Entrada')  # Field name made lowercase.
    salida = models.TimeField('Salida', db_column='Salida')  # Field name made lowercase.
    creado = models.DateTimeField(db_column='Creado')


    def __str__(self):
        return '%s' % (self.voluntario)

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        managed = False
        db_table = 'asistencia'