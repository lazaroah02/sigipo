from apps.core.test import TestCase
from apps.death_certificate.factories import DeathCertificateFactory


class DeathCertificateTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.death = DeathCertificateFactory.create()

    def test_deathCertificate_str(self):
        self.assertEqual(str(self.death), f"{self.death.patient}")
