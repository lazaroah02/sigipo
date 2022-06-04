from apps.core.test import TestCase
from apps.patient.factories import PatientFactory
from apps.patient.models import Patient


class PatientTestCase(TestCase):
    """Test case for Patient model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.patient = PatientFactory.create()
        cls.patient_oncologic = PatientFactory.create(is_oncologic=True)
        cls.patient_no_oncologic = PatientFactory.create(is_oncologic=False)

    def test_patient_str(self):
        """Test that patient str method returns the patient name."""
        self.assertEqual(
            str(self.patient),
            f"{self.patient.first_name} {self.patient.last_name} ({self.patient.identity_card})",
        )

    def test_queryset_manager_oncologic(self):
        """Test that queryset manager only returns oncologic patient."""
        self.assertNotIn(self.patient_no_oncologic, Patient.objects.only_oncologic())

    def test_queryset_manager_no_oncologic(self):
        """Test that queryset manager only returns no oncologic patient."""
        self.assertNotIn(self.patient_oncologic, Patient.objects.only_no_oncologic())
