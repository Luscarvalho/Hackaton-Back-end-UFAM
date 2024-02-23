from django.urls import path

from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView


urlpatterns = [
    path("", CategoriaListView.as_view(), name="categoria-list"),
    path("cadastrar", CategoriaCreateView.as_view(), name="categoria-create"),
    path("alterar/<int:pk>", CategoriaUpdateView.as_view(), name="categoria-update"),
    path("deletar/<int:pk>", CategoriaDeleteView.as_view(), name="categoria-delete"),
]
