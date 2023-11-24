from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import UpdateView, CreateView, DeleteView, ListView
from .models import Hospedagem
from .forms import HospedagemForm
from django.urls import reverse_lazy


class HospedagemListView(ListView):
    model = Hospedagem
    template_name = "aluno/hospedagens.html"
    context_object_name = "hospedagens"
    paginate_by = 2


class HospedagemCreateView(CreateView):
    model = Hospedagem
    template_name = "aluno/form.html"
    form_class = HospedagemForm
    success_url = reverse_lazy('home')


class HospedagemUpdateView(UpdateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = "aluno/form.html"
    success_url = reverse_lazy("home")


class HospedagemDeleteView(DeleteView):
    model = Hospedagem
    success_url = reverse_lazy("home")
    context_object_name = "hospedagem"
    template_name = "aluno/confirmacao_delecao.html"
