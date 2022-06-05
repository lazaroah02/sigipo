from django.core.exceptions import ValidationError

from apps.core.test import TestCase
from apps.geographic_location.factories import MunicipalityFactory
from apps.patient.forms import OncologicPatientForm
from apps.patient.validators import only_numbers_validator


class ValidatorTestCase(TestCase):
    """Test case for custom validators."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.municipality = MunicipalityFactory.create()
        cls.born_municipality = MunicipalityFactory.create()

    def test_validator_valid(self):
        """Test that validator returns true."""
        self.assertTrue(only_numbers_validator("2345"))

    def test_validator_invalid(self):
        """Test that validator returns ValidationError."""
        with self.assertRaises(ValidationError):
            only_numbers_validator("A2345")

    def test_validator_invalid_identity_card(self):
        """Test that validator returns ValidationError."""
        data = {
            "identity_card": "11111111111",
            "first_name": "1",
            "last_name": "1",
            "address": "1",
            "race": "1",
            "medical_record": "1",
            "age_at_diagnosis": "1",
            "residence_municipality": self.municipality.pk,
            "born_municipality": self.municipality.pk,
        }
        form = OncologicPatientForm(data=data)
        self.assertTrue(form.is_valid())
        data["identity_card"] = "1111111"
        form = OncologicPatientForm(data=data)
        self.assertFalse(form.is_valid())
