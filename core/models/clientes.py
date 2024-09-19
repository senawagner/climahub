from django.db import models
from django.core.exceptions import ValidationError

# Cliente (Empresa)
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    com_contrato = models.BooleanField(default=False)
    pmoc = models.BooleanField(default=False)  # Indica se o cliente segue PMOC
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']  # Opcional: ordena por nome

    def clean(self):
        # Exemplo de validação personalizada
        if self.com_contrato and not self.pmoc:
            raise ValidationError("Clientes com contrato devem seguir PMOC.")

    def __str__(self):
        return self.nome

# Cliente Pessoa Física
class ClientePessoaFisica(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Filiais de Clientes
class Filial(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='filiais')
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True, verbose_name="Ativa")

    class Meta:
        verbose_name = 'Filial'
        verbose_name_plural = 'Filiais'

    def __str__(self):
        return f'{self.nome} - {self.cliente.nome}'
