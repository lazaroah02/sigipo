from apps.core.test import TestCase
from apps.drugs.factories import DrugFactory, NuclearMedicineDrugFactory


class NuclearMedicineDrugTestCase(TestCase):
    """Test case for NuclearMedicineDrug model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.drug = NuclearMedicineDrugFactory.create()

    def test_drug_str(self):
        """Test that NuclearMedicineDrug str method returns the drug name."""
        self.assertEqual(
            str(self.drug),
            f"{self.drug.name}",
        )


class DrugTestCase(TestCase):
    """Test case for Drug model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.drug = DrugFactory.create()

    def test_drug_str(self):
        """Test that Drug str method returns the drug name."""
        self.assertEqual(
            str(self.drug),
            f"{self.drug.name} {self.drug.get_presentation_display()} {self.drug.amount} {self.drug.get_unit_display()}",
        )
