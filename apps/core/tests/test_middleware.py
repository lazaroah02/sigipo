# Create your tests here.
from http import HTTPStatus

from django.urls import reverse

from apps.accounts.factories import UserFactory
from apps.core.test import TestCase
from apps.geographic_location.factories import ProvinceFactory
from apps.geographic_location.models import Province


class BaseDeleteViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        province = ProvinceFactory.create()
        Province.objects.filter(pk=province.pk).delete()
        cls.invalid_pk = province.pk
        cls.province = ProvinceFactory.create()
        cls.superuser = UserFactory.create()
        cls.user_normal = UserFactory.create(
            username="normal", is_superuser=False, is_staff=False, is_active=False
        )

    def test_delete_superuser(self):
        self.client.force_login(self.superuser)
        response = self.client.post(
            reverse("geographic_location:province_delete", args=(self.invalid_pk,))
        )
        self.assertEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    def test_delete_normal_user(self):
        self.client.force_login(self.user_normal)
        response = self.client.post(
            reverse("geographic_location:province_delete", args=(self.invalid_pk,))
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
