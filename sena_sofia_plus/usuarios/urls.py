

from django.urls import path

from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('saludar/', views.saludar, name='saludo'),
    path('usuarios/', views.usuarios, name='usuarios'),
]

