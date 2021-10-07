#From django libs and models
from django.db import models


class Asistencia(models.Model):
    idasistencia = models.AutoField(primary_key=True)  # Field name made lowercase.
    voluntario = models.ForeignKey(
        'voluntario.voluntario',
        on_delete= models.CASCADE
        )  # Field name made lowercase.
    entrada = models.TimeField('Entrada')  # Field name made lowercase.
    salida = models.TimeField('Salida')  # Field name made lowercase.
    creado = models.DateTimeField()


    def __str__(self):
        return '%s' % (self.voluntario)

    """def save(self, *args, **kwargs):
        TO_DO: Crear un metodo en otro fichero 
        que utilice request.user.pk para sobreescribir
        cada movimiento con el usuario que este logeado
        y guardarlo en usuario de cada registro.
    """
