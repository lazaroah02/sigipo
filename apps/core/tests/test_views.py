from django.contrib.messages import get_messages
from django.urls import reverse, reverse_lazy
from django.views.generic.base import ContextMixin

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.core.views import CancelUrlMixin, ViewTitleMixin
from apps.geographic_location.factories import ProvinceFactory
from apps.geographic_location.models import Province
from apps.geographic_location.views import ProvinceDeleteView
from apps.neoplasm.factories import NeoplasmFactory


class CancelUrlMixinTestCase(TestCase):
    """Test case for CancelUrlMixin."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""

        class Helper(CancelUrlMixin, ContextMixin):
            cancel_url = "admin:login"

        cls.mixin = Helper()

    def test_mixin_get_context_data(self):
        """Test that get_context_data in CancelUrlMixin returns the cancel url."""
        self.assertIn("cancel_url", self.mixin.get_context_data())
        self.assertEqual(
            self.mixin.get_context_data()["cancel_url"],
            "admin:login",
        )

    def test_mixin_get_cancel_url(self):
        """Test that get_cancel_url in CancelUrlMixin returns the cancel url."""
        self.assertEqual(
            reverse_lazy("admin:login"),
            self.mixin.get_cancel_url(),
        )


class ViewTitleMixinTestCase(TestCase):
    """Test case for ViewTitleMixin."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""

        class Helper(ViewTitleMixin, ContextMixin):
            title = "randomtitle"

        cls.mixin = Helper()

    def test_mixin_get_context_data(self):
        """Test that get_context_data in ViewTitleMixin returns the title of the view."""
        self.assertIn("view_title", self.mixin.get_context_data())
        self.assertEqual(
            self.mixin.get_context_data()["view_title"],
            "randomtitle",
        )


class GetObjectErrorMixinTestCase(TestCase):
    """Test case for GetObjectErrorMixin."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        province = ProvinceFactory.create()
        Province.objects.filter(pk=province.pk).delete()
        cls.invalid_pk = province.pk
        cls.valid_pk = ProvinceFactory.create().pk
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test that GetObjectErrorMixin redirects to the cancel_url and alert the user."""
        response = self.client.get(
            reverse("geographic_location:province_detail", args=(self.invalid_pk,))
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Provincia no encontrada")
        response = self.client.get(
            reverse("geographic_location:province_detail", args=(self.valid_pk,))
        )
        self.assertIn(
            "object",
            response.context,
        )


class BaseDetailViewTestCase(TestCase):
    """Test case for BaseDetailView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.province_pk = ProvinceFactory.create().pk
        cls.neoplasm_pk = NeoplasmFactory.create().pk
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get_context_data(self):
        """Test that BaseDetailView makes the form readonly."""
        response = self.client.get(
            reverse("geographic_location:province_detail", args=(self.province_pk,))
        )
        self.assertIn("form", response.context)
        self.assertIn("readonly", response.content.decode())

    def test_get_context_data_disable_checkbox(self):
        """Test that BaseDetailView makes the form readonly and checkboxes disabled."""
        response = self.client.get(
            reverse("neoplasm:neoplasm_detail", args=(self.neoplasm_pk,))
        )
        self.assertIn("form", response.context)
        self.assertIn("disabled", response.content.decode())


class BaseDeleteViewTestCase(TestCase):
    """Test case for BaseDeleteView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.province = ProvinceFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_delete(self):
        """Test that BaseDeleteView alert the user when an instance is deleted."""
        response = self.client.post(
            reverse("geographic_location:province_delete", args=(self.province.pk,))
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            ProvinceDeleteView.success_message % self.province.__dict__,
        )
        self.assertRedirects(
            response,
            ProvinceDeleteView.success_url,
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
