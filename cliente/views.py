from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from .models import Cliente


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'cliente/list.html'


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = 'form.html'
    fields = ['nome', 'email']
    success_url = reverse_lazy('cliente-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastrar Cliente"
        context['botao'] = "Cadastrar"
        return context


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'form.html'
    fields = ['nome', 'email']
    success_url = reverse_lazy('cliente-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Cliente"
        context['botao'] = "Editar"
        return context


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'delete.html'
    success_url = reverse_lazy('cliente-list')
