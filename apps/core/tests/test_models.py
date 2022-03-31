from django.test import TestCase

from apps.core.models import SingletonModel


class SingletonModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.singleton_model = SingletonModel.load()

    def test_delete(self):
        self.singleton_model.delete()
        self.assertTrue(True)

    def test_save(self):
        self.singleton_model.pk = None
        self.singleton_model.save()
        self.assertTrue(True)
