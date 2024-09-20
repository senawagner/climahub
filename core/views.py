from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Cliente, OrdemServico, Contrato
from .forms import ClienteForm, OrdemServicoForm, ContratoForm

class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'dashboard.html'
    model = Cliente  # Você pode mudar isso para o modelo mais apropriado para o dashboard
    context_object_name = 'items'

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10

class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = 'cliente'

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente criado com sucesso!')
        return super().form_valid(form)

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente atualizado com sucesso!')
        return super().form_valid(form)

class OrdemServicoListView(LoginRequiredMixin, ListView):
    model = OrdemServico
    template_name = 'ordem_servico_list.html'
    context_object_name = 'ordens'
    paginate_by = 10

class OrdemServicoDetailView(LoginRequiredMixin, DetailView):
    model = OrdemServico
    template_name = 'ordem_servico_detail.html'
    context_object_name = 'ordem'

class OrdemServicoCreateView(LoginRequiredMixin, CreateView):
    model = OrdemServico
    form_class = OrdemServicoForm
    template_name = 'ordem_servico_form.html'
    success_url = reverse_lazy('ordem_servico_list')

    def form_valid(self, form):
        messages.success(self.request, 'Ordem de Serviço criada com sucesso!')
        return super().form_valid(form)

class OrdemServicoUpdateView(LoginRequiredMixin, UpdateView):
    model = OrdemServico
    form_class = OrdemServicoForm
    template_name = 'ordem_servico_form.html'
    success_url = reverse_lazy('ordem_servico_list')

    def form_valid(self, form):
        messages.success(self.request, 'Ordem de Serviço atualizada com sucesso!')
        return super().form_valid(form)

class ContratoListView(LoginRequiredMixin, ListView):
    model = Contrato
    template_name = 'contrato_list.html'
    context_object_name = 'contratos'
    paginate_by = 10

class ContratoDetailView(LoginRequiredMixin, DetailView):
    model = Contrato
    template_name = 'contrato_detail.html'
    context_object_name = 'contrato'

class ContratoCreateView(LoginRequiredMixin, CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'contrato_form.html'
    success_url = reverse_lazy('contrato_list')

    def form_valid(self, form):
        messages.success(self.request, 'Contrato criado com sucesso!')
        return super().form_valid(form)

class ContratoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'contrato_form.html'
    success_url = reverse_lazy('contrato_list')

    def form_valid(self, form):
        messages.success(self.request, 'Contrato atualizado com sucesso!')
        return super().form_valid(form)
