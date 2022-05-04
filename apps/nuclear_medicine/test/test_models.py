from apps.core.test import TestCase
from apps.nuclear_medicine.factories import (
    HormonalResultFactory,
    HormonalStudyFactory,
    OncologicResultFactory,
    OncologicStudyFactory,
)


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
            f"Muestra {str(self.study.sample_number).zfill(2)} {str(self.study.tests)}",
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
            f"Muestra {str(self.study.sample_number).zfill(2)} {str(self.study.tests)}",
        )


class HormonalResultTestCase(TestCase):
    """Test case for HormonalResult model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.result = HormonalResultFactory.create()

    def test_study_str(self):
        """Test that HormonalResult str method returns the sample number and tests."""
        self.assertEqual(
            str(self.result),
            f"Resultado de Muestra {str(self.result.hormonal_study.sample_number).zfill(2)} {str(self.result.hormonal_study.tests)}",
        )


class OncologicResultTestCase(TestCase):
    """Test case for OncologicResult model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.result = OncologicResultFactory.create()

    def test_study_str(self):
        """Test that OncologicResult str method returns the sample number and tests."""
        self.assertEqual(
            str(self.result),
            f"Resultado de Muestra {str(self.result.oncologic_study.sample_number).zfill(2)} {str(self.result.oncologic_study.tests)}",
        )
