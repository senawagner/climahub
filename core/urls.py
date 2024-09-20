from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/criar/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_edit'),
    path('ordens-servico/', views.OrdemServicoListView.as_view(), name='ordem_servico_list'),
    path('ordens-servico/<int:pk>/', views.OrdemServicoDetailView.as_view(), name='ordem_servico_detail'),
    path('ordens-servico/criar/', views.OrdemServicoCreateView.as_view(), name='ordem_servico_create'),
    path('ordens-servico/<int:pk>/editar/', views.OrdemServicoUpdateView.as_view(), name='ordem_servico_edit'),
    path('contratos/', views.ContratoListView.as_view(), name='contrato_list'),
    path('contratos/<int:pk>/', views.ContratoDetailView.as_view(), name='contrato_detail'),
    path('contratos/criar/', views.ContratoCreateView.as_view(), name='contrato_create'),
    path('contratos/<int:pk>/editar/', views.ContratoUpdateView.as_view(), name='contrato_edit'),
]
