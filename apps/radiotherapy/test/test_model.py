from apps.core.test import TestCase
from apps.radiotherapy.factories import (
    AccessoriesFactory,
    DosimetryPlanFactory,
    EnergyFactory,
    EquipmentFactory,
    MedicalTurnFactory,
    PrescriptionFactory,
    RiskOrgansFactory,
    TACStudyFactory,
)


class DosimetryPlanTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dsplan = DosimetryPlanFactory.create()

    def test_DosimetryPlanFactory_str(self):
        self.assertEqual(str(self.dsplan), f"{self.dsplan.patient}")


class EnergyTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.energy = EnergyFactory.create()

    def test_EnergyFactory_str(self):
        self.assertEqual(str(self.energy), f"{self.energy.energy}")


class EquipmentTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.equip = EquipmentFactory.create()

    def test_EquipmentFactory_str(self):
        self.assertEqual(str(self.equip), f"{self.equip.name}")


class AccessoriesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.accesory = AccessoriesFactory.create()

    def test_AccessoriesFactory_str(self):
        self.assertEqual(str(self.accesory), f"{self.accesory.name}")


class RiskOrgansTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.rorg = RiskOrgansFactory.create()

    def test_RiskOrgansFactory_str(self):
        self.assertEqual(str(self.rorg), f"{self.rorg.name}")


class PrescriptionTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.prescription = PrescriptionFactory.create()

    def test_PrescriptionFactory_str(self):
        self.assertEqual(str(self.prescription), f"{self.prescription.treatment_serie}")


class MedicalTurnTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mturn = MedicalTurnFactory.create()

    def test_MedicalTurnFactory_str(self):
        self.assertEqual(str(self.mturn.patient), f"{self.mturn.patient}")


class TACStudyTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tacstudy = TACStudyFactory.create()

    def test_TACStudyFactory_str(self):
        self.assertEqual(str(self.tacstudy), f"{self.tacstudy.patient}")
