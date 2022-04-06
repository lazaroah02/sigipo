from django.test import RequestFactory, TestCase


class SigipoTestCaseMixin:
    request_factory = RequestFactory()


class TestCase(SigipoTestCaseMixin, TestCase):
    pass
