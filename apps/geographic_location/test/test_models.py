from django.test import TestCase

from apps.geographic_location.factories import MunicipalityFactory, ProvinceFactory


class ProvinceTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.province = ProvinceFactory.create()

    def test_province_str(self):
        self.assertEqual(
            str(self.province),
            self.province.name,
        )


class MunicipalityTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.municipality = MunicipalityFactory.create()

    def test_municipality_str(self):
        self.assertEqual(
            str(self.municipality),
            self.municipality.name,
        )
