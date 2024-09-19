from django.db import models
from core.models import Cliente, ClientePessoaFisica, Filial

# Equipamentos
class Equipamento(models.Model):
    TIPO_CHOICES = [
        ('AR_CONDICIONADO', 'Ar Condicionado'),
        ('REFRIGERADOR', 'Refrigerador'),
        ('FREEZER', 'Freezer'),
        ('CORTINA_AR', 'Cortina de Ar'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='equipamentos', null=True, blank=True)
    cliente_pf = models.ForeignKey(ClientePessoaFisica, on_delete=models.CASCADE, related_name='equipamentos', null=True, blank=True)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, related_name='equipamentos', null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    capacidade = models.CharField(max_length=50)
    data_instalacao = models.DateField()
    ultima_manutencao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.marca} {self.modelo}"

    def get_proprietario(self):
        if self.cliente:
            return self.cliente
        elif self.cliente_pf:
            return self.cliente_pf
        elif self.filial:
            return self.filial.cliente
        else:
            return None
