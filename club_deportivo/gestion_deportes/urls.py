from django.urls import path
from . import views

app_name = 'gestion_deportes'

urlpatterns = [
    path('', views.lista_deportes, name='lista_deportes'),
    path('<int:pk>/', views.detalle_deporte, name='detalle_deporte'),
    path('crear/', views.crear_deporte, name='crear_deporte'),
    path('<int:pk>/editar/', views.editar_deporte, name='editar_deporte'),
    path('<int:pk>/eliminar/', views.eliminar_deporte, name='eliminar_deporte'),
]