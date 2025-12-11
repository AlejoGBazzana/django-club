from django.urls import path
from . import views

app_name = 'gestion_deportistas'

urlpatterns = [
    path('', views.lista_deportistas, name='lista_deportistas'),
    path('crear/', views.crear_deportista, name='crear_deportista'),
    path('<int:pk>/', views.detalle_deportista, name='detalle_deportista'),
    path('<int:pk>/editar/', views.editar_deportista, name='editar_deportista'),
    path('<int:pk>/eliminar/', views.eliminar_deportista, name='eliminar_deportista'),
]