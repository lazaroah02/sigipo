from django.test import TestCase

from apps.accounts.factories import UserFactory


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_without_name = UserFactory.create()
        cls.user_with_name = UserFactory.create(first_name="John", last_name="Doe")

    def test_user_with_name_str(self):
        self.assertEqual(
            str(self.user_with_name),
            (
                "%s %s"
                % (self.user_with_name.first_name, self.user_with_name.last_name)
            ).strip(),
        )

    def test_user_without_name_str(self):
        self.assertEqual(str(self.user_without_name), self.user_without_name.username)
