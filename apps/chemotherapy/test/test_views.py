from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.chemotherapy.factories import (
    CycleFactory,
    CycleMedicationFactory,
    ProtocolFactory,
)
from apps.chemotherapy.forms import CycleForm
from apps.chemotherapy.models import Cycle
from apps.core.test import TestCase
from apps.drugs.factories import DrugFactory


class CycleViewTestCase(TestCase):
    """Test case for Cycle views."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.cycle = CycleFactory.create()
        cls.cycle_medicine = CycleMedicationFactory.create(cycle=cls.cycle)
        cls.protocol = ProtocolFactory.create()
        cls.drug = DrugFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_cycle_get(self):
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

    def test_cycle_post(self):
        """Test Cycle view get."""
        cycle_count = Cycle.objects.count()
        self.client.post(
            reverse("chemotherapy:cycle_create"),
            {
                "protocol": self.protocol.pk,
                "next_date": "2020-01-01",
                "cyclemedication_set-0-drug": self.drug.pk,
                "cyclemedication_set-0-dose": "1",
                "cyclemedication_set-0-unit": "1",
                "cyclemedication_set-TOTAL_FORMS": 1,
                "cyclemedication_set-INITIAL_FORMS": 0,
                "cyclemedication_set-MIN_NUM_FORMS": 0,
                "cyclemedication_set-MAX_NUM_FORMS": 1000,
            },
        )
        self.assertTrue(Cycle.objects.count() == cycle_count + 1)
        response = self.client.post(
            reverse("chemotherapy:cycle_create"),
            {
                "protocol": self.protocol.pk,
                "next_date": "2020-01-01",
                "cyclemedication_set-0-drug": "",
                "cyclemedication_set-0-dose": "1",
                "cyclemedication_set-0-unit": "1",
                "cyclemedication_set-TOTAL_FORMS": 1,
                "cyclemedication_set-INITIAL_FORMS": 0,
                "cyclemedication_set-MIN_NUM_FORMS": 0,
                "cyclemedication_set-MAX_NUM_FORMS": 1000,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(self.cycle_medicine.drug.pk, self.drug.pk)
        self.client.post(
            reverse("chemotherapy:cycle_update", args=(self.cycle.pk,)),
            {
                "protocol": self.cycle.protocol.pk,
                "next_date": "2020-01-01",
                "cyclemedication_set-0-id": self.cycle_medicine.pk,
                "cyclemedication_set-0-drug": self.drug.pk,
                "cyclemedication_set-0-cycle": self.cycle.pk,
                "cyclemedication_set-0-dose": "1",
                "cyclemedication_set-0-unit": "1",
                "cyclemedication_set-TOTAL_FORMS": 2,
                "cyclemedication_set-INITIAL_FORMS": 1,
                "cyclemedication_set-MIN_NUM_FORMS": 0,
                "cyclemedication_set-MAX_NUM_FORMS": 1000,
            },
        )
        self.cycle_medicine.refresh_from_db()
        self.assertEqual(self.cycle_medicine.drug.pk, self.drug.pk)
        self.client.post(
            reverse("chemotherapy:cycle_update", args=(self.cycle.pk,)),
            {
                "protocol": self.cycle.protocol.pk,
                "next_date": "2020-01-01",
                "cyclemedication_set-0-id": self.cycle_medicine.pk,
                "cyclemedication_set-0-drug": self.drug.pk,
                "cyclemedication_set-0-cycle": self.cycle.pk,
                "cyclemedication_set-0-dose": "1",
                "cyclemedication_set-MAX_NUM_FORMS": 1000,
            },
        )
        self.assertEqual(response.status_code, 200)
