from django.db import models
from .clientes import Cliente
from django.core.exceptions import ValidationError
from django.utils import timezone

# Contratos
class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contratos', help_text="Cliente associado a este contrato")
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2, help_text="Valor do contrato")
    FREQUENCIA_CHOICES = [
        ('MENSAL', 'Mensal'),
        ('TRIMESTRAL', 'Trimestral'),
        ('SEMESTRAL', 'Semestral'),
        ('ANUAL', 'Anual'),
    ]
    frequencia_manutencao = models.CharField(max_length=20, choices=FREQUENCIA_CHOICES)
    ativo = models.BooleanField(default=True)
    descricao = models.TextField(blank=True, null=True, help_text="Descrição detalhada do contrato")

    def __str__(self):
        return f"Contrato {self.id} - {self.cliente.nome}"

    def clean(self):
        if self.data_fim and self.data_inicio and self.data_fim < self.data_inicio:
            raise ValidationError("A data de fim não pode ser anterior à data de início.")

    def duracao(self):
        if self.data_fim:
            return (self.data_fim - self.data_inicio).days
        return (timezone.now().date() - self.data_inicio).days

    def esta_ativo(self):
        return self.ativo and (not self.data_fim or self.data_fim >= timezone.now().date())

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['-data_inicio']  # Ordena por data de início, mais recente primeiro
