from apps.core.test import TestCase
from apps.geographic_location.factories import (
    LocationFactory,
    MunicipalityFactory,
    ProvinceFactory,
)


class ProvinceTestCase(TestCase):
    """Test case for Province model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.province = ProvinceFactory.create()

    def test_province_str(self):
        """Test that province str method returns the province name."""
        self.assertEqual(
            str(self.province),
            self.province.name,
        )


class MunicipalityTestCase(TestCase):
    """Test case for Municipality model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.municipality = MunicipalityFactory.create()

    def test_municipality_str(self):
        """Test that municipality str method returns the municipality name."""
        self.assertEqual(
            str(self.municipality),
            f"{self.municipality.name} - {self.municipality.province.name}",
        )


class LocationTestCase(TestCase):
    """Test case for Location model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.location = LocationFactory.create()

    def test_location_str(self):
        """Test that location str method returns the location name."""
        self.assertEqual(
            str(self.location),
            f"{self.location.name} - {self.location.municipality.name} - {self.location.municipality.province.name}",
        )
