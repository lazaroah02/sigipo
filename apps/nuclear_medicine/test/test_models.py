from apps.core.test import TestCase
from apps.nuclear_medicine.factories import OncologicStudyFactory


class OncologicStudyTestCase(TestCase):
    """Test case for OncologicStudy model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.study = OncologicStudyFactory.create()

    def test_study_str(self):
        """Test that OncologicStudy str method returns the province name."""
        self.assertEqual(
            str(self.study),
            f"Muestra {str(self.study.sample_number)} {str(self.study.tests)}",
        )
