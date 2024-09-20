from django import forms
from .models import Cliente, Contrato

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'tipo', 'email', 'telefone', 'cep', 'endereco', 'cpf', 'cnpj', 'razao_social']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].required = False
        self.fields['cnpj'].required = False
        self.fields['razao_social'].required = False

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')
        cpf = cleaned_data.get('cpf')
        cnpj = cleaned_data.get('cnpj')
        razao_social = cleaned_data.get('razao_social')

        if tipo == 'PF':
            if not cpf:
                self.add_error('cpf', 'CPF é obrigatório para Pessoa Física.')
        elif tipo == 'PJ':
            if not cnpj:
                self.add_error('cnpj', 'CNPJ é obrigatório para Pessoa Jurídica.')
            if not razao_social:
                self.add_error('razao_social', 'Razão Social é obrigatória para Pessoa Jurídica.')

        return cleaned_data

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['cliente', 'data_inicio', 'data_fim', 'valor', 'frequencia_manutencao', 'ativo', 'descricao']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')

        if data_inicio and data_fim and data_fim < data_inicio:
            raise forms.ValidationError("A data de fim não pode ser anterior à data de início.")

        return cleaned_data
