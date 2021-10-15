#imports from Django
from django.shortcuts import render
from datetime import *

#imports from models
from voluntario.models import Voluntario

#IMPORTES DE LIBRERIAS EXTERNAS
from easy_pdf.views import PDFTemplateView


class DiplomaPDF(PDFTemplateView):
    template_name = "voluntario/diploma.html"

    def get_context_data(self, **kwargs):
        id = self.request.GET.get("id")
        voluntario = None
        try:
            voluntario = Voluntario.objects.get(pk=id)
        except Voluntario.DoesNotExist:
            voluntario = None
        return super(DiplomaPDF, self).get_context_data(
                pagesize="Letter",
                title="Diploma",
                voluntario=voluntario,
                **kwargs
        )