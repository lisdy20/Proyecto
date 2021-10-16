"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from entidad.views import DonacionHistorialPDF, DonacionMensualesPDF
from ruta.views import RutaPDF
from voluntario.views import DiplomaPDF

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^ruta-de-riesgo/(?P<id>)" , RutaPDF.as_view()),
    url(r"^donaciones-mensuales/(?P<id>)" , DonacionMensualesPDF.as_view()),
    url(r"^historial-de-donaciones/(?P<id>)" , DonacionHistorialPDF.as_view()),
    url(r"^voluntario-diploma/(?P<id>)" , DiplomaPDF.as_view())
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)