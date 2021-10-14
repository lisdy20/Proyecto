from django.db import models

# Create your models here.

class Tipo(models.Model):
    idtipo = models.AutoField(db_column='IdTipo', primary_key=True)
    nombre = models.CharField('Tipo de la Donación', db_column='Nombre', max_length=75)
    
    
    def __str__(self):
        return '%s %s' % (self.nombre)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'