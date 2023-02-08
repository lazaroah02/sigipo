from apps.chemotherapy.factories import (
    CycleFactory,
    CycleMedicationFactory,
    MedicationFactory,
    ProtocolFactory,
    SchemeFactory,
)
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
        cls.protocol_1 = ProtocolFactory.create(suspended=True)

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

    def test_not_suspended_protocol(self):
        """Test that Protocol return the correct queryset."""
        self.assertNotIn(self.protocol_1, Protocol.objects.not_suspended())


class MedicationTestCase(TestCase):
    """Test case for Medication model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.medication = MedicationFactory.create()

    def test_medication_str(self):
        """Test that Medication str returns the drug and protocol."""
        self.assertEqual(
            str(self.medication),
            f"{self.medication.drug} en {self.medication.protocol}",
        )


class CycleTestCase(TestCase):
    """Test case for Cycle Model."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Common test data."""
        cls.cycle = CycleFactory.create()

    def test_cycle_str(self):
        """Test that Cycle str returns the protocol."""
        self.assertEqual(str(self.cycle), f"Ciclo de {self.cycle.protocol}")


class CycleMedicationTestCase(TestCase):
    """Test case for CycleMedication Model."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Common test data."""
        cls.cycle_medication = CycleMedicationFactory.create()

    def test_cycle_medication_str(self):
        """Test that CycleMedication str returns the drug and cycle."""
        self.assertEqual(
            str(self.cycle_medication),
            f"{self.cycle_medication.drug} en {self.cycle_medication.cycle}",
        )
