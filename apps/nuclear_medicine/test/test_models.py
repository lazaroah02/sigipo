from apps.core.test import TestCase
from apps.nuclear_medicine.factories import (
    HormonalResultFactory,
    HormonalStudyFactory,
    IodineDetectionFactory,
    OncologicResultFactory,
    OncologicStudyFactory,
    RadioIsotopeFactory,
    SerialIodineDetectionFactory,
    StudyFactory,
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


class SerialIodineDetectionTestCase(TestCase):
    """Test case for SerialIodineDetection model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.iodine_detection = SerialIodineDetectionFactory.create()

    def test_study_str(self):
        """Test that SerialIodineDetection str method returns the patient name."""
        self.assertEqual(
            str(self.iodine_detection),
            f"Detección de yodo seriada de {str(self.iodine_detection.patient)}",
        )


class IodineDetectionTestCase(TestCase):
    """Test case for IodineDetection model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.iodine_detection = IodineDetectionFactory.create()

    def test_study_str(self):
        """Test that IodineDetection str method returns the patient name."""
        self.assertEqual(
            str(self.iodine_detection),
            f"Detección de yodo de {str(self.iodine_detection.patient)}",
        )


class StudyTestCase(TestCase):
    """Test case for Study model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.study = StudyFactory.create()

    def test_study_str(self):
        """Test that Study str method returns the name."""
        self.assertEqual(
            str(self.study),
            f"{str(self.study.name)}",
        )


class RadioIsotopeTestCase(TestCase):
    """Test case for RadioIsotope model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.radio_isotope = RadioIsotopeFactory.create()

    def test_study_str(self):
        """Test that RadioIsotope str method returns name."""
        self.assertEqual(
            str(self.radio_isotope),
            f"{str(self.radio_isotope.name)}",
        )
