from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.nuclear_medicine.factories import OncologicStudyFactory


class OncologicStudyViewTestCase(TestCase):
    """Test case for OncologicStudy."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.study = OncologicStudyFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_detail_view(self):
        """Test the get method for OncologicStudyDetailView."""
        response = self.client.get(
            reverse("nuclear_medicine:oncologic_study_detail", args=(self.study.pk,))
        )
        self.assertIn(str(self.study.created_at.year), response.content.decode())
        self.assertIn(str(self.study.created_at.day), response.content.decode())
        self.assertIn(str(self.study.created_at.month), response.content.decode())
        self.assertIn(str(self.study.sample_number), response.content.decode())
