from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText

from apps.geographic_location.models import Municipality, Province


class ProvinceFactory(DjangoModelFactory):
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
            "Sáncti Spíritus",
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
    class Meta:
        model = Municipality

    province = SubFactory(ProvinceFactory)
    name = FuzzyText(prefix="Municipio-", length=20)
