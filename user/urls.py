from django.urls import path
from django.contrib.auth import views as auth_views
from user import views
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name='auth/login.html',
        authentication_form=CustomLoginForm
    ), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
