from django.urls import path
from aluno import views

urlpatterns = [
    path("", views.HospedagemListView.as_view(),
         name="home"),
    path("criar-hospedagem/", views.HospedagemCreateView.as_view(),
         name="hospedagem_criar"),
    path("editar-hospedagem/<int:pk>/",
         views.HospedagemUpdateView.as_view(), name="hospedagem_editar"),
    path("excluir-hospedagem/<int:pk>/",
         views.HospedagemDeleteView.as_view(), name="hospedagem_remover")
]
