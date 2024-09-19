from django.db import models
from .clientes import Cliente
from .contratos import Contrato
from .ordens_servico import OrdemServico
from django.core.exceptions import ValidationError
from django.utils import timezone

# Faturamento
class Faturamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, help_text="Cliente associado a este faturamento")
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, null=True, blank=True, help_text="Ordem de serviço relacionada, se aplicável")
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, null=True, blank=True, help_text="Contrato relacionado, se aplicável")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_emissao = models.DateField()
    data_vencimento = models.DateField()
    pago = models.BooleanField(default=False)
    numero_fatura = models.CharField(max_length=20, unique=True, help_text="Número único da fatura")

    def __str__(self):
        return f"Fatura {self.id} - {(self.cliente.nome if self.cliente else self.cliente_pf.nome)} - R${self.valor}"

    def clean(self):
        if self.data_vencimento < self.data_emissao:
            raise ValidationError("A data de vencimento não pode ser anterior à data de emissão.")
        if not self.ordem_servico and not self.contrato:
            raise ValidationError("O faturamento deve estar associado a uma ordem de serviço ou a um contrato.")

    def esta_atrasado(self):
        return not self.pago and self.data_vencimento < timezone.now().date()

    class Meta:
        verbose_name = 'Faturamento'
        verbose_name_plural = 'Faturamentos'
        ordering = ['-data_emissao']  # Ordena por data de emissão, mais recente primeiro

METODO_PAGAMENTO_CHOICES = [
    ('BOLETO', 'Boleto'),
    ('CARTAO', 'Cartão de Crédito'),
    ('PIX', 'PIX'),
    ('TRANSFERENCIA', 'Transferência Bancária'),
]
metodo_pagamento = models.CharField(max_length=20, choices=METODO_PAGAMENTO_CHOICES, null=True, blank=True, help_text="Método de pagamento utilizado")
