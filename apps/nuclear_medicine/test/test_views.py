from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.nuclear_medicine.factories import (
    OncologicResultFactory,
    OncologicStudyFactory,
)
from apps.nuclear_medicine.models import OncologicResult


class OncologicStudyViewTestCase(TestCase):
    """Test case for OncologicStudy."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.study = OncologicStudyFactory.create()
        cls.result = OncologicResultFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_list(self):
        """Test the list view to ensure the pagination context is filled correctly."""
        response = self.client.get(reverse("nuclear_medicine:oncologic_result_list"))
        self.assertEqual(
            response.context["crud_name"],
            OncologicResult._meta.verbose_name_plural.capitalize(),
        )

    def test_detail_view(self):
        """Test the get method for OncologicStudyDetailView."""
        response = self.client.get(
            reverse("nuclear_medicine:oncologicstudy_detail", args=(self.study.pk,))
        )
        self.assertIn(str(self.study.created_at.year), response.content.decode())
        self.assertIn(str(self.study.created_at.day), response.content.decode())
        self.assertIn(str(self.study.created_at.month), response.content.decode())
        self.assertIn(str(self.study.sample_number), response.content.decode())
