from apps.accounts.factories import UserFactory
from apps.core.test import TestCase


class UserTestCase(TestCase):
    """Test case for User model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.user_without_name = UserFactory.create()
        cls.user_with_name = UserFactory.create(first_name="John", last_name="Doe")

    def test_user_with_name_str(self):
        """Test that the user return the join of first and last name."""
        self.assertEqual(
            str(self.user_with_name),
            (
                "%s %s"
                % (self.user_with_name.first_name, self.user_with_name.last_name)
            ).strip(),
        )

    def test_user_without_name_str(self):
        """Test that the user return the username if has no first_name."""
        self.assertEqual(str(self.user_without_name), self.user_without_name.username)
