from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .contratos import Contrato
from .ordens_servico import OrdemServico

# Validador de CEP
cep_validator = RegexValidator(
    regex=r'^\d{5}-?\d{3}$',
    message="CEP deve estar no formato 00000-000 ou 00000000"
)

# Validador de CPF
cpf_validator = RegexValidator(
    regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    message="CPF deve estar no formato 000.000.000-00"
)

# Validador de CNPJ
cnpj_validator = RegexValidator(
    regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
    message="CNPJ deve estar no formato 00.000.000/0000-00"
)

# Cliente (Empresa)
class Cliente(models.Model):
    TIPO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=9, validators=[cep_validator], help_text="Formato: 00000-000")
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    com_contrato = models.BooleanField(default=False)
    pmoc = models.BooleanField(default=False)  # Indica se o cliente segue PMOC
    data_cadastro = models.DateTimeField(auto_now_add=True)
    contratos = models.ManyToManyField(Contrato, related_name='clientes', blank=True)
    ordens_servico = models.ManyToManyField(OrdemServico, related_name='clientes', blank=True)

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
