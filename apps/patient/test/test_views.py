from http import HTTPStatus

from django.contrib.messages import get_messages
from django.http import FileResponse
from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.patient.factories import PatientFactory
from apps.patient.forms import PatientChangeStatusForm
from apps.patient.models import Patient


class PatientViewTestCase(TestCase):
    """Test case for PatientViews."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.patient = PatientFactory.create(is_oncologic=False)
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_change_status_get(self):
        """Test PatientChangeStatus get."""
        response = self.client.get(reverse("patient:oncologic_change_status"))
        self.assertIsInstance(response.context["filter"], PatientChangeStatusForm)
        self.assertEqual(response.context["object"], None)

    def test_change_status_get_filter(self):
        """Test that PatientChangeStatus returns the correct object."""
        not_found_patient = PatientFactory.create()
        Patient.objects.filter(pk=not_found_patient.pk).delete()
        response = self.client.get(
            reverse("patient:oncologic_change_status")
            + f"?identity_card={self.patient.identity_card}&medical_record={self.patient.medical_record}"
        )
        self.assertEqual(response.context["object"], self.patient)
        response = self.client.get(
            reverse("patient:oncologic_change_status")
            + f"?identity_card={not_found_patient.identity_card}&medical_record={not_found_patient.medical_record}"
        )
        self.assertEqual(response.context["object"], True)
        self.assertIn("No hay datos registrados.", response.content.decode())

    def test_change_status_confirmation_error(self):
        """Test PatientChangeStatus confirmation screen."""
        not_found_patient = PatientFactory.create()
        Patient.objects.filter(pk=not_found_patient.pk).delete()
        response = self.client.get(
            reverse(
                "patient:oncologic_change_status_confirmation",
                args=(not_found_patient.pk,),
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    def test_change_status_confirmation_get(self):
        """Test PatientChangeStatus confirmation screen."""
        response = self.client.get(
            reverse(
                "patient:oncologic_change_status_confirmation",
                args=(self.patient.pk,),
            )
        )
        self.assertIn(self.patient.first_name, response.content.decode())

    def test_change_status_confirmation(self):
        """Test PatientChangeStatus confirmation screen."""
        response = self.client.post(
            reverse(
                "patient:oncologic_change_status_confirmation",
                args=(self.patient.pk,),
            )
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "Estado de paciente actualizado.",
        )
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.is_oncologic, True)

    def test_check_patient_created(self):
        """Test check_patient_created view."""
        response = self.client.get(
            reverse(
                "patient:check_patient_created",
                args=(self.patient.identity_card,),
            )
        )
        self.assertTrue(response.json()["exist"])

    def test_patient_create_as_popup(self):
        """Test the create view in popup mode."""
        response = self.client.get(
            reverse(
                "patient:oncologic_create",
            )
            + "is_popup=true"
        )
        self.assertNotIn(
            '<nav class="navbar navbar-expand-lg navbar-dark bg-gradient-primary">',
            response.content.decode(),
        )

    def test_patient_create_as_popup_close_template(self):
        """Test the create view in popup mode.
        Test that the patient is created and the popup is closed."""
        self.patient.delete()
        patient_count = Patient.objects.count()
        response = self.client.post(
            reverse(
                "patient:oncologic_create",
            )
            + "?is_popup=true",
            {
                "identity_card": self.patient.identity_card,
                "first_name": self.patient.first_name,
                "last_name": self.patient.last_name,
                "residence_municipality": self.patient.residence_municipality.pk,
                "born_municipality": self.patient.residence_municipality.pk,
                "race": 0,
                "sex": 0,
            },
        )
        self.assertEqual(patient_count + 1, Patient.objects.count())
        response = self.client._handle_redirects(response)
        self.assertRedirects(response, reverse("close_popup"))
        self.assertTemplateUsed(response, "components/close_popup.html")


class PatientExportTestCase(TestCase):
    """Test case for Neoplasm Export."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.patient = PatientFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_export(self):
        """Test the patient report response."""
        response = self.client.post(
            reverse("patient:patient_list"),
        )
        self.assertIsInstance(response, FileResponse)


class OncologicPatientExportTestCase(TestCase):
    """Test case for Neoplasm Export."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.patient = PatientFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_export(self):
        """Test the oncologic patient report response."""
        response = self.client.post(
            reverse("patient:oncologic_list"),
        )
        self.assertIsInstance(response, FileResponse)
