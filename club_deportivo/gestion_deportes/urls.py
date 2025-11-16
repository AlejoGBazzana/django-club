from django.urls import path
from .views import lista_deportes

urlpatterns = [
    path('', lista_deportes, name='lista_deportes'),
]