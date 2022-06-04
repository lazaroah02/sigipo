from django.core.exceptions import ValidationError

from apps.core.test import SimpleTestCase
from apps.patient.validators import only_numbers_validator


class ValidatorTestCase(SimpleTestCase):
    """Test case for custom validators."""

    def test_validator_valid(self):
        """Test that validator returns true."""
        self.assertTrue(only_numbers_validator("2345"))

    def test_validator_invalid(self):
        """Test that validator returns false."""
        with self.assertRaises(ValidationError):
            only_numbers_validator("A2345")
