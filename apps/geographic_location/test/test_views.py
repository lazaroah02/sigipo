from http import HTTPStatus

from django.contrib.messages import get_messages
from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.geographic_location.factories import MunicipalityFactory, ProvinceFactory
from apps.geographic_location.forms import MunicipalityForm, ProvinceForm
from apps.geographic_location.models import Municipality, Province
from apps.geographic_location.views import (
    MunicipalityCreateView,
    MunicipalityDeleteView,
    MunicipalityDetailView,
    MunicipalityUpdateView,
    ProvinceCreateView,
    ProvinceDeleteView,
    ProvinceDetailView,
    ProvinceUpdateView,
)


class ProvinceDetailViewTestCase(TestCase):
    """Test case for ProvinceDetailView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.province = ProvinceFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for ProvinceDetailView."""
        response = self.client.get(
            reverse("geographic_location:province_detail", args=(self.province.pk,))
        )
        self.assertIn(str(self.province), response.content.decode())
        self.assertIn("form", response.context)
        self.assertIn("readonly", response.content.decode())
        self.assertIn(reverse(ProvinceDetailView.cancel_url), response.content.decode())


class ProvinceDeleteViewTestCase(TestCase):
    """Test case for ProvinceDeleteView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.province = ProvinceFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_post(self):
        """Test the post method for ProvinceDeleteView."""
        response = self.client.post(
            reverse("geographic_location:province_delete", args=(self.province.pk,))
        )
        self.assertFalse(Province.objects.filter(pk=self.province.pk).exists())

    def test_get(self):
        """Test the get method for ProvinceDeleteView."""
        response = self.client.get(
            reverse("geographic_location:province_delete", args=(self.province.pk,))
        )
        self.assertIn(str(self.province), response.content.decode())
        self.assertIn(reverse(ProvinceDeleteView.cancel_url), response.content.decode())


class ProvinceCreateViewTestCase(TestCase):
    """Test case for ProvinceCreateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for ProvinceCreateView."""
        response = self.client.get(reverse("geographic_location:province_create"))
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], ProvinceForm))
        self.assertIn(reverse(ProvinceCreateView.cancel_url), response.content.decode())

    def test_post(self):
        """Test the post method for ProvinceCreateView."""
        count_before_test = Province.objects.count()
        response = self.client.post(
            reverse("geographic_location:province_create"), {"name": "TestProvince"}
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            ProvinceCreateView.success_message % {"name": "TestProvince"},
        )
        self.assertEqual(Province.objects.count(), count_before_test + 1)


class ProvinceUpdateViewTestCase(TestCase):
    """Test case for ProvinceUpdateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.province = ProvinceFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for ProvinceUpdateView."""
        response = self.client.get(
            reverse("geographic_location:province_update", args=(self.province.pk,))
        )
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], ProvinceForm))
        self.assertIn(reverse(ProvinceUpdateView.cancel_url), response.content.decode())

    def test_post(self):
        """Test the post method for ProvinceUpdateView."""
        response = self.client.post(
            reverse("geographic_location:province_update", args=(self.province.pk,)),
            {"name": "TestProvince"},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            ProvinceUpdateView.success_message % {"name": "TestProvince"},
        )
        self.province.refresh_from_db()
        self.assertEqual(str(self.province), "TestProvince")


class MunicipalityDetailViewTestCase(TestCase):
    """Test case for MunicipalityDetailView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.municipality = MunicipalityFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for MunicipalityDetailView."""
        response = self.client.get(
            reverse(
                "geographic_location:municipality_detail", args=(self.municipality.pk,)
            )
        )
        self.assertIn(self.municipality.name, response.content.decode())
        self.assertIn(self.municipality.province.name, response.content.decode())
        self.assertIn("form", response.context)
        self.assertIn("readonly", response.content.decode())
        self.assertIn(
            reverse(MunicipalityDetailView.cancel_url), response.content.decode()
        )


class MunicipalityDeleteViewTestCase(TestCase):
    """Test case for MunicipalityDeleteView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.municipality = MunicipalityFactory.create()
        cls.user = UserFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_post(self):
        """Test the post method for MunicipalityDeleteView."""
        self.client.post(
            reverse(
                "geographic_location:municipality_delete", args=(self.municipality.pk,)
            )
        )
        self.assertFalse(Municipality.objects.filter(pk=self.municipality.pk).exists())

    def test_get(self):
        """Test the get method for MunicipalityDeleteView."""
        response = self.client.get(
            reverse(
                "geographic_location:municipality_delete", args=(self.municipality.pk,)
            )
        )
        self.assertIn(str(self.municipality), response.content.decode())
        self.assertIn(
            reverse(MunicipalityDeleteView.cancel_url), response.content.decode()
        )


class MunicipalityCreateViewTestCase(TestCase):
    """Test case for MunicipalityCreateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.province = ProvinceFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for MunicipalityCreateView."""
        response = self.client.get(reverse("geographic_location:municipality_create"))
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], MunicipalityForm))
        self.assertIn(reverse(ProvinceCreateView.cancel_url), response.content.decode())

    def test_post(self):
        """Test the post method for MunicipalityCreateView."""
        count_before_test = Municipality.objects.count()
        response = self.client.post(
            reverse("geographic_location:municipality_create"),
            {"name": "TestMunicipality", "province": self.province.pk},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            MunicipalityCreateView.success_message % {"name": "TestMunicipality"},
        )
        self.assertEqual(Municipality.objects.count(), count_before_test + 1)


class MunicipalityUpdateViewTestCase(TestCase):
    """Test case for MunicipalityUpdateView."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user = UserFactory.create()
        cls.province = ProvinceFactory.create(name="TestProvince")
        cls.municipality = MunicipalityFactory.create()

    def setUp(self) -> None:
        """Extra initialization."""
        self.client.force_login(self.user)

    def test_get(self):
        """Test the get method for MunicipalityUpdateView."""
        response = self.client.get(
            reverse(
                "geographic_location:municipality_update", args=(self.municipality.pk,)
            )
        )
        self.assertIn("form", response.context)
        self.assertTrue(isinstance(response.context["form"], MunicipalityForm))
        self.assertIn(
            reverse(MunicipalityUpdateView.cancel_url), response.content.decode()
        )

    def test_post(self):
        """Test the post method for MunicipalityUpdateView."""
        response = self.client.post(
            reverse(
                "geographic_location:municipality_update", args=(self.municipality.pk,)
            ),
            {"name": "TestMunicipality", "province": self.province.pk},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            MunicipalityUpdateView.success_message % {"name": "TestMunicipality"},
        )
        self.municipality.refresh_from_db()
        self.assertEqual(str(self.municipality), "TestMunicipality - TestProvince")
        self.assertEqual(self.municipality.province.pk, self.province.pk)
