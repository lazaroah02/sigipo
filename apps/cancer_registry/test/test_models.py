from apps.cancer_registry.factories import NeoplasmFactory, TNMFactory
from apps.core.test import TestCase


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


class TNMTestCase(TestCase):
    """Test case for TNM model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.tnm = TNMFactory.create(
            patient__first_name="Test",
            patient__last_name="Test",
            patient__medical_record="Test",
        )

    def test_neoplasm_str(self):
        """Test that tnm str method returns the patient name tumor nodule and metastasis."""
        self.assertEqual(
            str(self.tnm),
            f"Test Test (Test) {self.tnm.tumor} {self.tnm.nodule} {self.tnm.metastasis}",
        )
