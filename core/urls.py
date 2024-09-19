from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.cliente_edit, name='cliente_edit'),
    path('ordens-servico/', views.ordem_servico_list, name='ordem_servico_list'),
    path('ordens-servico/<int:pk>/', views.ordem_servico_detail, name='ordem_servico_detail'),
    path('ordens-servico/nova/', views.ordem_servico_create, name='ordem_servico_create'),
    path('ordens-servico/<int:pk>/editar/', views.ordem_servico_edit, name='ordem_servico_edit'),
    path('contratos/', views.contrato_list, name='contrato_list'),
    path('contratos/<int:pk>/', views.contrato_detail, name='contrato_detail'),
    path('contratos/novo/', views.contrato_create, name='contrato_create'),
    path('contratos/<int:pk>/editar/', views.contrato_edit, name='contrato_edit'),
]
