from django.test import TestCase
from .models import Plan

# Create your tests here.

class PlanTestCase(TestCase):
    def setUp(self):
        Plan.objects.create(
            titulo="Plan XS",
            velocidad="50 Megas",
            minutos=1000,
            canales="100 Canales",
            valor=25990
        )

        Plan.objects.create(
            titulo="Plan S",
            velocidad="70 Megas",
            minutos=2000,
            canales="120 Canales",
            valor=30990
        )


    def test_plan_valor(self):
        plan = Plan.objects.get(titulo="Plan XS")
        self.assertEqual(plan.valor, 27990)


    def test_plan_minutos(self):
        plan = Plan.objects.get(titulo="Plan S")
        self.assertEqual(plan.minutos, 2000)