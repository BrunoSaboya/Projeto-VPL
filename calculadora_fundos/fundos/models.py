from django.db import models

class FundoInvestimento(models.Model):
    cnpj_fundo = models.CharField(max_length=18)
    dt_comptc = models.DateField()
    vl_quota = models.DecimalField(max_digits=30, decimal_places=10)

    class Meta:
        db_table = 'fundos_investimento'  # Nome da tabela existente no banco de dados
        unique_together = ['cnpj_fundo', 'dt_comptc']
        indexes = [
            models.Index(fields=['cnpj_fundo', 'dt_comptc']),
        ]