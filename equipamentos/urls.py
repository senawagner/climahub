from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipamento_list, name='equipamento_list'),
    path('<int:pk>/', views.equipamento_detail, name='equipamento_detail'),
    path('novo/', views.equipamento_create, name='equipamento_create'),
    path('<int:pk>/editar/', views.equipamento_edit, name='equipamento_edit'),
]
