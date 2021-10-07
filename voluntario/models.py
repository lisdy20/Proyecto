#from django libs
from django.db import models
from creencias.models import Creencias
from authuser.models import AuthUser
from asistencia.models import Asistencia
from diasdevoluntariado.models import Diasdevoluntariado


#from third libs or python native
from datetime import * 

class Voluntario(models.Model):

    GENERO_CHOICE = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OTRO'),
    )

    TIPO_VOLUNTARIO = (
        ('L', 'LOCAL'),
        ('N', 'NACIONAL'),
        ('I', 'INTERNACIONAL'),
    )

    idvoluntario = models.AutoField(db_column='IdVoluntario', primary_key=True) 
    nombre = models.CharField('Nombre', db_column='Nombre', max_length=50) 
    apellido = models.CharField('Apellido', db_column='Apellido', max_length=50)
    telefono = models.CharField('Teléfono', db_column='Telefono', max_length=16) 
    genero = models.CharField('Género', db_column='Genero', choices=GENERO_CHOICE , max_length=1) 
    edad = models.IntegerField('Edad', db_column='Edad') 
    fechanacimiento = models.DateField('Fecha de Nacimiento', db_column='FechaNacimiento') 
    nacionalidad = models.CharField('Nacionalidad', db_column='Nacionalidad', max_length=50)
    correo = models.CharField(
        'Correo Electrónico' , 
        help_text="Ingresa tu correo ejemplo: correo@dominio.com",
        max_length=75,
        blank=True,
        null=True
        )  
    direccion = models.CharField('Dirección', db_column='Direccion', max_length=120) 
    tipovoluntario = models.CharField('Tipo de Voluntario', db_column='TipoVoluntario', choices=TIPO_VOLUNTARIO , max_length=1)  
    creencias = models.ForeignKey(Creencias, models.DO_NOTHING, db_column='FKCreenciasReligiosas')  # Field name made lowercase.
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='FKIdUsuario')
    

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

    def asistencia(self):
        asistencias = Asistencia.objects.filter(voluntario_id=self.pk)
        tiempo_total = 0
        """
            TO_DO // CALCULATE TOTAL HOUR ASSITED
        """
        return asistencias.count()
    

    def dias_voluntariado(self):
        """
            Funcion para mostrar los dias y las horas 
            que el voluntario prestara servicio.
        """

        dias = Diasdevoluntariado.objects.filter(voluntario_id=self.pk)
        array = []
        for d in dias:
            array.append('[{} - {}hrs]'.format(d.diaarealizar , d.horasaprox))
        print(array)
        return array


    class Meta:
        verbose_name = 'Voluntario'
        verbose_name_plural = 'Voluntarios'
        managed = False
        db_table = 'voluntario'