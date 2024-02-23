from django.urls import path

from .views import QuartoListView, QuartoCreateView, QuartoUpdateView, QuartoDeleteView


urlpatterns = [
    path("", QuartoListView.as_view(), name="quarto-list"),
    path("cadastrar", QuartoCreateView.as_view(), name="quarto-create"),
    path("alterar/<int:pk>", QuartoUpdateView.as_view(), name="quarto-update"),
    path("deletar/<int:pk>", QuartoDeleteView.as_view(), name="quarto-delete"),
]
