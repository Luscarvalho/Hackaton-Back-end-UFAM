from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from .models import Quarto


class QuartoListView(LoginRequiredMixin, ListView):
    model = Quarto
    template_name = 'quarto/list.html'


class QuartoCreateView(LoginRequiredMixin, CreateView):
    model = Quarto
    template_name = 'form.html'
    fields = ['descricao', 'idcategoria']
    success_url = reverse_lazy('quarto-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastrar Quarto"
        context['botao'] = "Cadastrar"
        return context


class QuartoUpdateView(LoginRequiredMixin, UpdateView):
    model = Quarto
    template_name = 'form.html'
    fields = ['descricao', 'idcategoria']
    success_url = reverse_lazy('quarto-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Quarto"
        context['botao'] = "Editar"
        return context


class QuartoDeleteView(LoginRequiredMixin, DeleteView):
    model = Quarto
    template_name = 'delete.html'
    success_url = reverse_lazy('quarto-list')
