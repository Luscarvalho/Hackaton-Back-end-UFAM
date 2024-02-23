from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from .models import Reserva
from .form import ReservaModelForm


class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'reserva/list.html'


class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = ReservaModelForm
    template_name = 'form.html'
    # fields = ['dt_inicial', 'dt_final', 'idclient', 'idquarto']
    success_url = reverse_lazy('reserva-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastrar Reserva"
        context['botao'] = "Cadastrar"
        return context


class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    template_name = 'form.html'
    fields = ['descricao', 'idcategoria']
    success_url = reverse_lazy('reserva-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Reserva"
        context['botao'] = "Editar"
        return context


class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = 'delete.html'
    success_url = reverse_lazy('reserva-list')
