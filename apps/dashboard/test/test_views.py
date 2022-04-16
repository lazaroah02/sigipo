from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.patient.factories import PatientFactory
from apps.patient.models import Patient


class DashboardTestCase(TestCase):
    """Test case for Dashboard view."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        Patient.objects.all().delete()
        cls.patient = PatientFactory.create(
            is_oncologic=True,
            born_municipality__province__name="Holguín",
            residence_municipality__province__name="Guantánamo",
        )
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get_template(self) -> None:
        """Test that the view returns the response."""
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertIsInstance(response, TemplateResponse)

    def test_get_county_data(self) -> None:
        """Test that the view returns the correct data."""
        response = self.client.get(reverse("dashboard:dashboard") + "?data=county")
        self.assertIsInstance(response, JsonResponse)

    def test_get_born_data(self) -> None:
        """Test that the view returns the correct data."""
        response = self.client.get(reverse("dashboard:dashboard") + "?data=born")
        self.assertIsInstance(response, JsonResponse)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(["cu-ho", 1], data[0])

    def test_get_residence_data(self) -> None:
        """Test that the view returns the correct data."""
        response = self.client.get(reverse("dashboard:dashboard") + "?data=residence")
        self.assertIsInstance(response, JsonResponse)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(["cu-gu", 1], data[0])
