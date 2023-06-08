from http import HTTPStatus

from django.contrib.messages import get_messages
from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.radiotherapy.factories import (
    DosimetryPlanFactory, 
    EnergyFactory, 
    EquipmentFactory, 
    AccessoriesFactory, 
    RiskOrgansFactory, 
    PrescriptionFactory, 
    MedicalTurnFactory, 
    TACStudyFactory,
    )
from apps.radiotherapy.forms import (
    DosimetryPlanForm,
    EnergyForm,
    EquipmentForm,
    AccessoriesForm,
    RiskOrgansForm,
    PrescriptionForm,
    MedicalTurnForm,
    TACStudyForm,
)

from apps.radiotherapy.models import (
    DosimetryPlan,
    Energy,
    Equipment,
    Accessories,
    RiskOrgans,
    Prescription,
    MedicalTurn,
    TACStudy,
)


class DosimetryPlanDetailViewTestCase(TestCase):
    """Test case for DeathCertificateDetailView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.dsmplan = DosimetryPlanFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for DosimetryPlanDetailViewTestCase."""
        response = self.client.get(
            reverse("radiotherapy:dosimetryplan_detail", args=(self.dsmplan.pk,))
        )
        self.assertIn(str(self.dsmplan), response.content.decode())
        self.assertIn("form", response.context)
        self.assertIn("readonly", response.content.decode())
