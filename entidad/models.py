from django.db import models

# Create your models here.

class Entidad(models.Model):
    identidad = models.AutoField(db_column='IdEntidad', primary_key=True)
    nombre = models.CharField('Nombre o Entidad', db_column='Nombre', max_length=200)


    def __str__(self):
        return '%s' % (self.nombre)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'