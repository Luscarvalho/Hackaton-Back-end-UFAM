from django.urls import path

from .views import ReservaListView, ReservaCreateView, ReservaUpdateView, ReservaDeleteView


urlpatterns = [
    path("", ReservaListView.as_view(), name="reserva-list"),
    path("cadastrar", ReservaCreateView.as_view(), name="reserva-create"),
    path("alterar/<int:pk>", ReservaUpdateView.as_view(), name="reserva-update"),
    path("deletar/<int:pk>", ReservaDeleteView.as_view(), name="reserva-delete"),
]
