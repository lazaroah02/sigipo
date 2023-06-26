from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.pathologic_anathomy.factories import BiopsyRequestFactory
from apps.pathologic_anathomy.forms import BiopsyRequestForm


class BiopsyRequestCreateViewTestCase(TestCase):
    """Test case for NeoplasmCreateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.biopsy_request = BiopsyRequestFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for NeoplasmCreateView."""
        response = self.client.get(reverse("pathologic_anathomy:biopsyrequest_list"))
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], BiopsyRequestForm))
