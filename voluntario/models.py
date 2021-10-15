#from django libs
import datetime
from django.db import models
from creencias.models import Creencias
from authuser.models import AuthUser
from asistencia.models import Asistencia
from diasdevoluntariado.models import Diasdevoluntariado
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe




#from third libs or python native
from datetime import timedelta
from django.utils import timezone


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
    usuario = models.ForeignKey(User, models.DO_NOTHING, db_column='FKIdUsuario')
    

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

    def asistencia(self):
        """
            -El query asistencias trae todas las asistencias registradas
            de un voluntario, luego se traducen a timedelta para poder
            operarlas de forma nativa con python.
            -Como pivote se establece tiempo_total a 00:00:00 en formato
            timedelta y asi poder hacer la suma total de las horas asistidas.
        """
        asistencias = Asistencia.objects.filter(voluntario_id=self.pk)
        tiempo_total = datetime.timedelta(hours=0 , minutes=0 , seconds=0)
        for a in asistencias:
            hora_entrada = str(a.entrada).split(':')
            hora_salida = str(a.salida).split(':')
            time_entrada = datetime.timedelta(
                hours=int(hora_entrada[0]) , 
                minutes=int(hora_entrada[1]), 
                seconds=int(hora_entrada[2])
                )
            time_salida = datetime.timedelta(
                hours=int(hora_salida[0]) , 
                minutes=int(hora_salida[1]),
                seconds=int(hora_salida[2])
                )
            resultado = time_salida - time_entrada
            tiempo_total = tiempo_total +  resultado
        return "{}.hrs".format(tiempo_total)
    
    def edad(self):
        try:
            cadena = int((timezone.now().date() - self.fechanacimiento).days / 365.25)
            return cadena
        except:
            cadena = []
            return cadena

    def dias_voluntariado(self):
        """
            Funcion para mostrar los dias y las horas 
            que el voluntario prestara servicio.
        """

        dias = Diasdevoluntariado.objects.filter(voluntario_id=self.pk)
        array = []
        for d in dias:
            array.append('[{} - {}hrs]'.format(d.diaarealizar , d.horasaprox))
        return array

    def diploma(self):
        return mark_safe(u'<a href="/voluntario-diploma/?id=%s" target="_blank" class="addlink">Diploma</a>'% self.pk)
