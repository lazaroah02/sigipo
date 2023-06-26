import datetime
from apps.core.test import TestCase
from apps.pathologic_anathomy.factories import BiopsyRequestFactory


class BiopsyResquestTest(TestCase):
    """Test case for Biopsy Request model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.biopsy_request = BiopsyRequestFactory.create()

    def test_biopsyrequest_str(self):
        """Test that Biopsy Request str method returns the biopsy id."""
        year = datetime.date.today().year
        self.assertEqual(
            str(self.biopsy_request),
            f"{year}-B-{self.biopsy_request.pk}",
        )
