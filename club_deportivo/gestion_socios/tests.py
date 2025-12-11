from django.test import TestCase
from django.urls import reverse
from .models import Socio

class SocioModelTest(TestCase):
    def test_crear_socio(self):
        socio = Socio.objects.create(
            nombre="Juan",
            apellido="Perez",
            email="juan@example.com"
        )
        self.assertEqual(str(socio), "Juan Perez")
        self.assertEqual(Socio.objects.count(), 1)

class SocioViewTest(TestCase):
    def setUp(self):
        self.socio = Socio.objects.create(
            nombre="Maria",
            apellido="Gomez",
            email="maria@example.com"
        )

    def test_lista_socios_view(self):
        response = self.client.get(reverse('gestion_socios:lista_socios'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maria Gomez")

    def test_detalle_socio_view(self):
        response = self.client.get(reverse('gestion_socios:detalle_socio', args=[self.socio.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "maria@example.com")