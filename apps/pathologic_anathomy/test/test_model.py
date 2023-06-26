from apps.core.test import TestCase
from apps.pathologic_anathomy.factories import BiopsyRequestFactory


class BiopsyResquestTest(TestCase):
    """Test case for Biopsy Request model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.BiopsyRequest = BiopsyRequestFactory.create()

    def test_biopsyrequest_str(self):
        """Test that Biopsy Request str method returns the biopsy id."""
        self.assertEqual(
            str(self.BiopsyRequest),
            "2023-B-1",
        )
