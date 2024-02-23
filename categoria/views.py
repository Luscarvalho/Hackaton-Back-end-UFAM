from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from .models import Categoria


class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria/list.html'


class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'form.html'
    fields = ['descricao', 'valor']
    success_url = reverse_lazy('categoria-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastrar Categoria"
        context['botao'] = "Cadastrar"
        return context


class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'form.html'
    fields = ['descricao', 'valor']
    success_url = reverse_lazy('categoria-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Categoria"
        context['botao'] = "Editar"
        return context


class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'delete.html'
    success_url = reverse_lazy('categoria-list')
