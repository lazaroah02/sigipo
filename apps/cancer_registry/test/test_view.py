from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.cancer_registry.forms import NeoplasmForm
from apps.cancer_registry.views import NeoplasmCreateView
from apps.core.test import TestCase


class NeoplasmCreateViewTestCase(TestCase):
    """Test case for NeoplasmCreateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for NeoplasmCreateView."""
        response = self.client.get(reverse("cancer_registry:neoplasm_create"))
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], NeoplasmForm))
        self.assertIn(
            "(None, '----------')",
            str(response.context["form"].fields["laterality"]._choices),
        )
        self.assertIn(reverse(NeoplasmCreateView.cancel_url), response.content.decode())
