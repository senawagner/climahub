from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente, OrdemServico, Contrato
from .forms import ClienteForm  
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Lógica para o dashboard
    return render(request, 'core/dashboard.html')

@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/cliente_list.html', {'clientes': clientes})

@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'core/cliente_detail.html', {'cliente': cliente})

@login_required
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, 'Cliente criado com sucesso!')
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'core/cliente_form.html', {'form': form})

@login_required
def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/cliente_form.html', {'form': form, 'cliente': cliente})

@login_required
def ordem_servico_list(request):
    ordens = OrdemServico.objects.all()
    return render(request, 'core/ordem_servico_list.html', {'ordens': ordens})

@login_required
def ordem_servico_detail(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    return render(request, 'core/ordem_servico_detail.html', {'ordem': ordem})

@login_required
def ordem_servico_create(request):
    # Lógica para criar uma nova ordem de serviço
    if request.method == 'POST':
        # Processar o formulário
        pass
    return render(request, 'core/ordem_servico_form.html')

@login_required
def ordem_servico_edit(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    # Lógica para editar uma ordem de serviço
    if request.method == 'POST':
        # Processar o formulário
        pass
    return render(request, 'core/ordem_servico_form.html', {'ordem': ordem})

@login_required
def contrato_list(request):
    contratos = Contrato.objects.all()
    return render(request, 'core/contrato_list.html', {'contratos': contratos})

@login_required
def contrato_detail(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    return render(request, 'core/contrato_detail.html', {'contrato': contrato})

@login_required
def contrato_create(request):
    # Lógica para criar um novo contrato
    if request.method == 'POST':
        # Processar o formulário
        pass
    return render(request, 'core/contrato_form.html')

@login_required
def contrato_edit(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    # Lógica para editar um contrato
    if request.method == 'POST':
        # Processar o formulário
        pass
    return render(request, 'core/contrato_form.html', {'contrato': contrato})
