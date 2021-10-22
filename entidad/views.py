#imports from Django
from django.shortcuts import render
from datetime import *

#imports from models
from donacion.models import Donacion

#IMPORTES DE LIBRERIAS EXTERNAS
from easy_pdf.views import PDFTemplateView

from tipodonacion.models import Tipodonacion


#custom functions
def inicial_day(date):
    """Date spliter.
    """
    split= date.split('-')
    init_date = '{}-{}-01 00:00:00'.format(split[0],split[1])
    return init_date

def fecha_con_hora(fecha):
    """
        receive a simple date to conver a timestamp.
        tipical use in filter queries.
    """
    if fecha:
        fs = fecha.split('-')
        date = datetime(int(fs[0]) , int(fs[1]) , int(fs[2]) , 23 , 59 , 59 , 00000)
        return date
    else:
        date = []
        return date

class DonacionMensualesPDF(PDFTemplateView):
    template_name = "entidad/donaciones.html"

    def get_context_data(self, **kwargs):
        id = self.request.GET.get("id")
        today = datetime.today().strftime("%Y-%m-%d")
        init = inicial_day(today)
        final = fecha_con_hora(today)
        donaciones = Donacion.objects.filter(nombre__pk=id , fechadeentrega__range=[init, final])
        ids = []
        for d in donaciones:
            ids.append(d.pk)
        detalle = Tipodonacion.objects.filter(donacion__pk__in=ids)
        return super(DonacionMensualesPDF, self).get_context_data(
                pagesize="Letter",
                title="Donaciones mensuales",
                donaciones=donaciones,
                detalle = detalle,
                init = init,
                final = final,
                **kwargs
        )

class DonacionHistorialPDF(PDFTemplateView):
    template_name = "entidad/donaciones_historico.html"

    def get_context_data(self, **kwargs):
        id = self.request.GET.get("id")
        donaciones = Donacion.objects.filter(nombre__pk=id)
        ids = []
        for d in donaciones:
            ids.append(d.pk)
        detalle = Tipodonacion.objects.filter(donacion__pk__in=ids)
        return super(DonacionHistorialPDF, self).get_context_data(
                pagesize="Letter",
                title="Donaciones mensuales",
                donaciones=donaciones,
                detalle = detalle,
                **kwargs
        )