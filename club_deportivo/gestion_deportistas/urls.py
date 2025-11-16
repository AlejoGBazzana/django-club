from django.urls import path
from .views import lista_deportistas

app_name = 'gestion_deportistas'

urlpatterns = [
    path('', lista_deportistas, name='lista_deportistas'),
]