from apps.cancer_registry.factories import NeoplasmFactory
from apps.core.test import TestCase


class NeoplasmTestCase(TestCase):
    """Test case for Neoplasm model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.neoplasm = NeoplasmFactory.create(
            patient__first_name="Test",
            patient__last_name="Test",
            patient__identity_card="123456",
            primary_site__name="TEST LOCATION",
        )

    def test_neoplasm_str(self):
        """Test that neoplasm str method returns the patient name."""
        self.assertEqual(
            str(self.neoplasm),
            "Test Test (123456) TEST LOCATION",
        )
