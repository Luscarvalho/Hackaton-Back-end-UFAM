from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls')),
    path('categoria/', include('categoria.urls')),
    path('quarto/', include('quarto.urls')),
    path('reserva/', include('reserva.urls')),
]
