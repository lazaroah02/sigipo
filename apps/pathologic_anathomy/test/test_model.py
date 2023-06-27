import datetime

from apps.core.test import TestCase
from apps.pathologic_anathomy.factories import BiopsyRequestFactory
from apps.pathologic_anathomy.models import BiopsyRequest


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
            f"{year}-B-{self.biopsy_request.pk} {self.biopsy_request.get_biopsy_type_display()}",
        )

    def test_save_method_creates_biopsy_id(self):
        # Step 1: Creates an instance of the class that has the function save
        instance = BiopsyRequest()
        self.assertIsNone(instance.biopsy_id)
        # Step 2: Call the method save in the instance
        instance.save()
        # step 3: Verify the atribute biopsy_id it's been fully establish
        year = datetime.date.today().year
        expected_biopsy_id = f"{year}-B-{instance.pk}"
        self.assertEqual(instance.biopsy_id, expected_biopsy_id)

    def test_save_method_does_not_overwrite_biopsy_id(self):
        # Create an instance of the model with a biopsy_id
        model_instance = BiopsyRequest(biopsy_id="biopsy_id", biopsy_id="2022-B-1")
        # Save the instance
        model_instance.save()
        # Ensure the biopsy_id was not overwritten
        self.assertEqual(model_instance.biopsy_id, "2022-B-1")
