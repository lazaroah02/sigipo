from django.db.models import CharField, IntegerChoices, IntegerField, Model


class DrugTypeChoices(IntegerChoices):
    CONCOMITANT = 0, "Concomitante"
    CYTOSTATIC = 1, "Citostático"


class Drug(Model):
    name = CharField(max_length=100, verbose_name="Nombre")
    drug_type = IntegerField(choices=DrugTypeChoices.choices, verbose_name="Tipo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Fármaco"
        verbose_name_plural = "Fármacos"
        ordering = ["pk"]
        default_permissions = ()
