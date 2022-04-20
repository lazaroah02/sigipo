from apps.core.test import TestCase
from apps.neoplasm.factories import NeoplasmFactory


class NeoplasmTestCase(TestCase):
    """Test case for Neoplasm model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.neoplasm = NeoplasmFactory.create(
            patient__first_name="Test",
            patient__last_name="Test",
            patient__medical_record="Test",
        )

    def test_neoplasm_str(self):
        """Test that neoplasm str method returns the patient name."""
        self.assertEqual(
            str(self.neoplasm),
            "Test Test (Test)",
        )
