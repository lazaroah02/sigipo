from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText

from apps.geographic_location.models import Municipality, Province


class ProvinceFactory(DjangoModelFactory):
    """Factory to handle province creation."""

    class Meta:
        model = Province

    name = FuzzyChoice(
        (
            "Pinar del Río",
            "La Habana",
            "Artemisa" "Mayabeque",
            "Matanzas",
            "Villa Clara",
            "Cienfuegos",
            "Sancti Spíritus",
            "Ciego de Ávila",
            "Camagüey",
            "Las Tunas",
            "Holguín",
            "Granma",
            "Santiago de Cuba",
            "Guantánamo",
            "Isla de la Juventud",
        )
    )


class MunicipalityFactory(DjangoModelFactory):
    """Factory to handle municipality creation."""

    class Meta:
        model = Municipality

    province = SubFactory(ProvinceFactory)
    name = FuzzyText(prefix="Municipio-", length=20)
