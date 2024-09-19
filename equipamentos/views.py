from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipamento, Manutencao

@login_required
def equipamento_list(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos/equipamento_list.html', {'equipamentos': equipamentos})

@login_required
def equipamento_detail(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    return render(request, 'equipamentos/equipamento_detail.html', {'equipamento': equipamento})

@login_required
def equipamento_create(request):
    if request.method == 'POST':
        # Lógica para processar o formulário de criação
        # Você pode usar um ModelForm aqui para facilitar a validação e salvamento
        pass
    return render(request, 'equipamentos/equipamento_form.html')

@login_required
def equipamento_edit(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        # Lógica para processar o formulário de edição
        pass
    return render(request, 'equipamentos/equipamento_form.html', {'equipamento': equipamento})

@login_required
def manutencao_list(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    manutencoes = Manutencao.objects.filter(equipamento=equipamento)
    return render(request, 'equipamentos/manutencao_list.html', {
        'equipamento': equipamento,
        'manutencoes': manutencoes
    })

@login_required
def manutencao_create(request, equipamento_pk):
    equipamento = get_object_or_404(Equipamento, pk=equipamento_pk)
    if request.method == 'POST':
        # Lógica para processar o formulário de criação de manutenção
        pass
    return render(request, 'equipamentos/manutencao_form.html', {'equipamento': equipamento})

@login_required
def manutencao_edit(request, pk):
    manutencao = get_object_or_404(Manutencao, pk=pk)
    if request.method == 'POST':
        # Lógica para processar o formulário de edição de manutenção
        pass
    return render(request, 'equipamentos/manutencao_form.html', {'manutencao': manutencao})
