from apps.core.test import TestCase
from apps.nuclear_medicine.factories import HormonalStudyFactory, OncologicStudyFactory


class OncologicStudyTestCase(TestCase):
    """Test case for OncologicStudy model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.study = OncologicStudyFactory.create()

    def test_study_str(self):
        """Test that OncologicStudy str method returns the sample number and tests."""
        self.assertEqual(
            str(self.study),
            f"Muestra {str(self.study.sample_number)} {str(self.study.tests)}",
        )


class HormonalStudyTestCase(TestCase):
    """Test case for HormonalStudy model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.study = HormonalStudyFactory.create()

    def test_study_str(self):
        """Test that HormonalStudy str method returns the sample number and tests."""
        self.assertEqual(
            str(self.study),
            f"Muestra {str(self.study.sample_number)} {str(self.study.tests)}",
        )
