from apps.core.test import SimpleTestCase
from apps.patient.filters import CustomRangeWidget


class CustomRangeWidgetTestCase(SimpleTestCase):
    """Test case for CustomRangeWidget."""

    def test_filter(self):
        """Test that the custom widget sets the placeholder."""
        html_str = str(CustomRangeWidget().render("test", None))
        self.assertIn("Edad de diagnóstico mínima", html_str)
        self.assertIn("Edad de diagnóstico máxima", html_str)
