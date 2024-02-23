from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
    path('categoria/', include('categoria.urls')),
    # path('', include('quarto.urls')),
    # path('', include('reserva.urls')),
]
