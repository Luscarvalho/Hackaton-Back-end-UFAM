from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cliente.urls')),
    path('categoria/', include('categoria.urls')),
    path('quarto/', include('quarto.urls')),
    # path('', include('reserva.urls')),
]
