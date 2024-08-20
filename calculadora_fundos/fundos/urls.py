from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^api/retorno/(?P<cnpj_fundo>[0-9\.\-\"/"]+)/$', views.calcular_retorno),
]