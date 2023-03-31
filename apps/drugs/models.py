from django.db.models import (
    BooleanField,
    CharField,
    FloatField,
    IntegerChoices,
    IntegerField,
    Model,
)


class DrugTypeChoices(IntegerChoices):
    CYTOSTATIC = 0, "Citostático"
    IMMUNO_MODULATOR = 1, "Inmuno Modulador"
    MONOCLONAL_ANTIBODY = 2, "Anticuerpo Monoclonal"
    CONCOMITANT = 3, "Concomitante"
    BIFOSFONATE = 4, "Bifosfonato"
    THERAPEUTIC_VACCINE = 5, "Vacuna Terapeutica"


class PresentationChoicesChoices(IntegerChoices):
    BULB = 0, "Bulbo"
    AMPOULE = 1, "Ámpula"
    FRASCO = 2, "Frasco"
    COMPRESSED = 3, "Comprimido"
    PILL = 4, "Píldora"
    TABLET = 5, "Pastilla"


class UnitChoicesChoices(IntegerChoices):
    M = 0, "g"
    MG = 1, "mg"
    ML = 2, "ml"


class NuclearMedicineDrug(Model):
    name = CharField(max_length=100, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fármaco de medicina nuclear"
        verbose_name_plural = "Fármacos de medicina nuclear"
        ordering = ["pk"]


class Drug(Model):
    name = CharField(max_length=100, verbose_name="Nombre")
    drug_type = IntegerField(choices=DrugTypeChoices.choices, verbose_name="Tipo")
    presentation = IntegerField(
        choices=PresentationChoicesChoices.choices,
        verbose_name="Presentación",
        null=True,
        blank=True,
    )
    amount = FloatField(verbose_name="Cantidad")
    unit = IntegerField(
        verbose_name="Unidad", null=True, blank=True, choices=UnitChoicesChoices.choices
    )
    out_of_stock = BooleanField(verbose_name="¿En falta?")

    def __str__(self):
        return f"{self.name} {self.get_presentation_display()} {self.amount} {self.get_unit_display()}"

    class Meta:
        verbose_name = "Fármaco de quimioterapia"
        verbose_name_plural = "Fármacos de quimioterapia"
        ordering = ["pk"]
