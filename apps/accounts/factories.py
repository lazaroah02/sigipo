from factory import Faker
from factory.django import DjangoModelFactory

from apps.accounts.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = Faker("user_name", locale="en_US")
    email = Faker("safe_email", locale="en_US")
    password = Faker("password", locale="en_US")
    is_superuser = True
    is_staff = True
