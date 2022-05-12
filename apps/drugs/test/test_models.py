from apps.core.test import TestCase
from apps.drugs.factories import DrugFactory


class SerialIodineDetectionTestCase(TestCase):
    """Test case for SerialIodineDetection model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.drug = DrugFactory.create()

    def test_drug_str(self):
        """Test that Drug str method returns the drug name."""
        self.assertEqual(
            str(self.drug),
            f"{self.drug.name}",
        )
