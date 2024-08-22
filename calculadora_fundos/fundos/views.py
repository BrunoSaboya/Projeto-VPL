from django.http import JsonResponse
from .models import FundoInvestimento
from django.shortcuts import get_object_or_404
from django.shortcuts import render

def index(request):
    return render(request, 'fundos/index.html')

def calcular_retorno(request, cnpj_fundo):
    try:
        print(f"Consultando CNPJ: {cnpj_fundo}")
        # Busca o valor da cota do dia 1 de julho de 2024)
        quota_inicio = FundoInvestimento.objects.filter(cnpj_fundo=cnpj_fundo, dt_comptc='2024-07-01').order_by('id').first().vl_quota
        
        # Busca o valor da cota do dia 31 de julho de 2024
        quota_fim = FundoInvestimento.objects.filter(cnpj_fundo=cnpj_fundo, dt_comptc='2024-07-31').order_by('id').first().vl_quota
        print(f"Quotas início: {quota_inicio}")
        print(f"Quotas fim: {quota_fim}")

        # Calcula o retorno
        retorno = (quota_fim / quota_inicio) - 1
        
        return JsonResponse({'cnpj_fundo': cnpj_fundo, 'retorno': float(retorno)})
    except FundoInvestimento.DoesNotExist:
        return JsonResponse({'error': 'Dados não encontrados para este fundo.'}, status=404)
    except FundoInvestimento.MultipleObjectsReturned:
        return JsonResponse({'error': 'Erro inesperado: múltiplos registros encontrados.'}, status=500)