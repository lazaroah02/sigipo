from apps.chemotherapy.factories import ProtocolFactory, SchemeFactory
from apps.chemotherapy.models import Protocol
from apps.core.test import TestCase


class SchemeTestCase(TestCase):
    """Test case for Scheme model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.scheme = SchemeFactory.create(name="ASDF-1234")

    def test_scheme_str(self):
        """Test that Scheme str method returns the Scheme name."""
        self.assertEqual(
            str(self.scheme),
            "ASDF-1234",
        )


class ProtocolTestCase(TestCase):
    """Test case for Protocol model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.protocol = ProtocolFactory.create(weight=64.0, height=175)

    def test_protocol_str(self):
        """Test that Protocol str method returns the Protocol name."""
        self.assertEqual(
            str(self.protocol),
            f"Protocolo de {self.protocol.patient} con esquema {self.protocol.scheme}",
        )

    def test_body_surface_str(self):
        """Test that Protocol returns the correct body surface."""
        self.assertEqual(
            Protocol.objects.first().body_surface,
            1.78,
        )
