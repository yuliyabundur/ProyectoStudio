from django.test import TestCase
from AppBeautyStudio.models import Especialista

# Create your tests here.
class URLTest(TestCase):

    def test_inicio(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class TestModels(TestCase):

    def setUp(self):
        self.especialista1 = Especialista.objects.create(
            nombre = 'Especialista de ejemplo 1',
            apellidos = 'Apellido de ejemplo 1',
            profesion = 'Alguna profesion'
        )

    def test_modulo(self):
        self.assertEquals(self.especialista1.nombre, 'Especialista de ejemplo 1')
        self.assertEquals(self.especialista1.profesion, 'Alguna profesion')