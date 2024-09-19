from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

from equipamentos.models import Equipamento
from .clientes import Cliente, ClientePessoaFisica, Filial
from .contratos import Contrato

# Adicione esta importação no topo do arquivo
from django.db.models import TextChoices

# Adicione estas definições antes da classe OrdemServico
class Status(TextChoices):
    ABERTA = 'ABERTA', 'Aberta'
    EM_ANDAMENTO = 'EM_ANDAMENTO', 'Em Andamento'
    CONCLUIDA = 'CONCLUIDA', 'Concluída'
    CANCELADA = 'CANCELADA', 'Cancelada'

class Tipo(TextChoices):
    PREVENTIVA = 'PREVENTIVA', 'Preventiva'
    CORRETIVA = 'CORRETIVA', 'Corretiva'
    INSTALACAO = 'INSTALACAO', 'Instalação'

class Prioridade(TextChoices):
    BAIXA = 'BAIXA', 'Baixa'
    MEDIA = 'MEDIA', 'Média'
    ALTA = 'ALTA', 'Alta'
    URGENTE = 'URGENTE', 'Urgente'

# Ordens de Serviço
class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ordens_servico', null=True, blank=True, help_text="Cliente associado à ordem de serviço")
    cliente_pf = models.ForeignKey(ClientePessoaFisica, on_delete=models.CASCADE, related_name='ordens_servico', null=True, blank=True)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, related_name='ordens_servico', null=True, blank=True)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='ordens_servico')
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    prioridade = models.CharField(max_length=20, choices=Prioridade.choices, default=Prioridade.MEDIA)
    descricao = models.TextField()
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_agendamento = models.DateTimeField(null=True, blank=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ABERTA)
    tecnico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"OS {self.id} - {self.get_tipo_display()} - {(self.cliente.nome if self.cliente else self.cliente_pf.nome)}"

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
        ordering = ['-data_abertura']

    def clean(self):
        if not self.cliente and not self.cliente_pf and not self.filial:
            raise ValidationError("É necessário especificar um cliente, cliente pessoa física ou filial.")
        if self.data_conclusao and self.data_conclusao < self.data_abertura:
            raise ValidationError("A data de conclusão não pode ser anterior à data de abertura.")

    def duracao(self):
        if self.data_conclusao:
            return (self.data_conclusao - self.data_abertura).days
        return (timezone.now() - self.data_abertura).days

    def esta_atrasada(self):
        return self.status != 'CONCLUIDA' and self.data_agendamento and self.data_agendamento < timezone.now().date()

    def get_status_display(self):
        base_status = self.get_status_display()
        if self.status == self.Status.EM_ANDAMENTO and self.esta_atrasada():
            return f"{base_status} (Atrasada)"
        return base_status

class Manutencao(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    data_realizacao = models.DateTimeField()
    descricao = models.TextField()
    pecas_substituidas = models.TextField(blank=True)
    observacoes = models.TextField(blank=True)
    tecnico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='manutencoes_realizadas')
    PRIORIDADE_CHOICES = [
        ('BAIXA', 'Baixa'),
        ('MEDIA', 'Média'),
        ('ALTA', 'Alta'),
        ('URGENTE', 'Urgente'),
    ]
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default='MEDIA')

    def __str__(self):
        return f"Manutenção {self.id} - OS {self.ordem_servico.id}"

    class Meta:
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'
        ordering = ['-data_realizacao']
