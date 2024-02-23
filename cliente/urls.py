from django.urls import path

from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView


urlpatterns = [
    path("", ClienteListView.as_view(), name="cliente-list"),
    path("cadastrar", ClienteCreateView.as_view(), name="cliente-create"),
    path("alterar/<int:pk>", ClienteUpdateView.as_view(), name="cliente-update"),
    path("deletar/<int:pk>", ClienteDeleteView.as_view(), name="cliente-delete"),
]
