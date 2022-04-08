from django.test import RequestFactory, TestCase


class SigipoTestCaseMixin:
    """Mixin to add request_factory to all test cases."""

    request_factory = RequestFactory()


class TestCase(SigipoTestCaseMixin, TestCase):
    """Custom test case to be used in all tests."""

    pass
