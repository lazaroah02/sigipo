from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.chemotherapy.factories import CycleFactory, CycleMedicationFactory
from apps.chemotherapy.forms import CycleForm
from apps.core.test import TestCase


class CycleViewTestCase(TestCase):
    """Test case for Cycle views."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.cycle = CycleFactory.create()
        cls.cycle_medicine = CycleMedicationFactory.create(cycle=cls.cycle)
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_cycle_create_get(self):
        """Test Cycle view get."""
        response = self.client.get(reverse("chemotherapy:cycle_create"))
        self.assertIsInstance(response.context["form"], CycleForm)
        self.assertIn("form-check-input", response.content.decode())
        response = self.client.get(
            reverse("chemotherapy:cycle_update", args=(self.cycle.pk,))
        )
        self.assertIsInstance(response.context["form"], CycleForm)
        self.assertIn("form-check-input", response.content.decode())
        response = self.client.get(
            reverse("chemotherapy:cycle_detail", args=(self.cycle.pk,))
        )
        self.assertIn("form", response.context)
        self.assertIn("form-check-input", response.content.decode())
