from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.pathologic_anathomy.factories import BiopsyRequestFactory
from apps.pathologic_anathomy.forms import BiopsyRequestForm
from apps.pathologic_anathomy.models import BiopsyRequest


class BiopsyRequestCreateViewTestCase(TestCase):
    """Test case for BiopsyRequest"""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.biopsy_request = BiopsyRequestFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_list(self):
        """Test the get method for biopsy request view."""
        response = self.client.get(reverse("pathologic_anathomy:biopsyrequest_list"))
        self.assertEqual(
            response.context["crud_name"],
            BiopsyRequest._meta.verbose_name_plural.capitalize(),
        )
        self.assertIn(str(self.biopsy_request.biopsy_id), response.content.decode())
        

