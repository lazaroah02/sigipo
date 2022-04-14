from apps.classifiers.factories import MorphologyFactory, TopographyFactory
from apps.core.test import TestCase


class MorphologyTestCase(TestCase):
    """Test case for Morphology model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.morphology = MorphologyFactory.create()

    def test_Morphology_str(self):
        """Test that morphology str method returns the morphology description."""
        self.assertEqual(
            str(self.morphology),
            f"{self.morphology.description}",
        )


class TopographyTestCase(TestCase):
    """Test case for Topography model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.topography = TopographyFactory.create()

    def test_Morphology_str(self):
        """Test that morphology str method returns the topography description."""
        self.assertEqual(
            str(self.topography),
            f"{self.topography.description}",
        )
