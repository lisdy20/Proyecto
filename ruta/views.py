from django.shortcuts import render

#IMPORTE DE MODELS
from ruta.models import Ruta

#IMPORTES DE LIBRERIAS EXTERNAS
from easy_pdf.views import PDFTemplateView


class RutaPDF(PDFTemplateView):
    template_name = "ruta/ruta.html"

    def get_context_data(self, **kwargs):
        id = self.request.GET.get("id")
        ruta = Ruta.objects.get(pk=id)

        return super(RutaPDF, self).get_context_data(
                pagesize="Letter",
                title="RUTA",
                ruta=ruta,
                **kwargs
        )