from django.test import TestCase
from django.urls import reverse
from .models import Deporte

class DeporteModelTest(TestCase):
    def test_crear_deporte(self):
        deporte = Deporte.objects.create(nombre="Futbol")
        self.assertEqual(str(deporte), "Futbol")

class DeporteViewTest(TestCase):
    def setUp(self):
        self.deporte = Deporte.objects.create(nombre="Tenis")

    def test_lista_deportes_view(self):
        response = self.client.get(reverse('gestion_deportes:lista_deportes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tenis")