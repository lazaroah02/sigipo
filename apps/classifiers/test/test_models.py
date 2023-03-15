from apps.classifiers.factories import (
    MorphologyFactory,
    RadioIsotopeFactory,
    StudyFactory,
    TopographyFactory,
)
from apps.core.test import TestCase


class MorphologyTestCase(TestCase):
    """Test case for Morphology model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.morphology = MorphologyFactory.create()

    def test_Morphology_str(self):
        """Test that morphology str method returns the morphology name."""
        self.assertEqual(
            str(self.morphology),
            f"{self.morphology.name}",
        )


class TopographyTestCase(TestCase):
    """Test case for Topography model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.topography = TopographyFactory.create()

    def test_Morphology_str(self):
        """Test that morphology str method returns the topography name."""
        self.assertEqual(
            str(self.topography),
            f"{self.topography.name}",
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

    def test_radio_isotope_str(self):
        """Test that RadioIsotope str method returns name."""
        self.assertEqual(
            str(self.radio_isotope),
            f"{str(self.radio_isotope.name)}",
        )
