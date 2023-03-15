from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from apps.death_certificate.models import DeathCertificate


class DeathCertificateFactory(DjangoModelFactory):
    """Factory to handle death_certificate creation."""

    class Meta:
        model = DeathCertificate

    name = FuzzyText(length=20)
