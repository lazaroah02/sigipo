from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.neoplasm.factories import NeoplasmFactory
from apps.neoplasm.models import Neoplasm
from apps.patient.factories import PatientFactory
from apps.patient.models import Patient


class DashboardTestCase(TestCase):
    """Test case for Dashboard view."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.patient = PatientFactory.create(
            is_oncologic=True,
            born_municipality__province__name="Holguín",
            residence_municipality__province__name="Guantánamo",
        )
        cls.neoplasm = NeoplasmFactory.create(
            patient__is_oncologic=True,
            patient__age_at_diagnosis=19,
        )
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get_template(self) -> None:
        """Test that the view returns the response."""
        Patient.objects.exclude(pk=self.patient.pk).delete()
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertIsInstance(response, TemplateResponse)

    def test_get_county_data(self) -> None:
        """Test that the view returns the correct data."""
        Patient.objects.exclude(pk=self.patient.pk).delete()
        response = self.client.get(reverse("dashboard:dashboard") + "?data=county")
        self.assertIsInstance(response, JsonResponse)

    def test_get_born_data(self) -> None:
        """Test that the view returns the correct data."""
        Patient.objects.exclude(pk=self.patient.pk).delete()
        response = self.client.get(reverse("dashboard:dashboard") + "?data=born")
        self.assertIsInstance(response, JsonResponse)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(["cu-ho", 1], data[0])

    def test_get_residence_data(self) -> None:
        """Test that the view returns the correct data."""
        Patient.objects.exclude(pk=self.patient.pk).delete()
        response = self.client.get(reverse("dashboard:dashboard") + "?data=residence")
        self.assertIsInstance(response, JsonResponse)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(["cu-gu", 1], data[0])

    def test_get_top_ten_data(self) -> None:
        """Test that the view returns the correct data."""
        Neoplasm.objects.exclude(pk=self.neoplasm.pk).delete()
        response = self.client.get(reverse("dashboard:dashboard") + "?data=top10")
        self.assertIsInstance(response, JsonResponse)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(
            {
                "primary_site__code": self.neoplasm.primary_site.code,
                "primary_site__description": self.neoplasm.primary_site.description,
                "less_than_20": 1,
                "num_subjects": 1,
                "patient_in_20s": 0,
                "patient_in_30s": 0,
                "patient_in_40s": 0,
                "patient_in_50s": 0,
                "patient_in_60s": 0,
                "patient_in_70s": 0,
                "patient_more_than_80s": 0,
            },
            data[0],
        )
