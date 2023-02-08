from import_export.resources import Field, ModelResource

from apps.patient.models import Patient


class PatientResource(ModelResource):
    """Resource for Patient model."""

    identity_card = Field(attribute="identity_card", column_name="Carnet de identidad")
    first_name = Field(attribute="first_name", column_name="Nombre")
    last_name = Field(attribute="last_name", column_name="Apellidos")
    street = Field(attribute="street", column_name="Calle")
    number = Field(attribute="number", column_name="Número")
    building = Field(attribute="building", column_name="Edificio")
    apartment = Field(attribute="apartment", column_name="Apartamento")
    sex = Field(attribute="sex", column_name="Sexo")
    date_of_birth = Field(attribute="date_of_birth", column_name="Fecha de nacimiento")
    between_streets = Field(attribute="between_streets", column_name="Entre calles")
    division = Field(attribute="division", column_name="Reparto")
    race = Field(attribute="race", column_name="Raza")
    medical_record = Field(
        attribute="medical_record", column_name="No. Historia Clínica"
    )
    residence_municipality = Field(
        attribute="residence_municipality", column_name="Municipio de residencia"
    )
    born_municipality = Field(
        attribute="born_municipality", column_name="Municipio natal"
    )
    is_oncologic = Field(attribute="is_oncologic", column_name="¿Es oncológico?")

    def dehydrate_sex(self, neoplasm):
        """Returns the sex in str format."""
        return str(neoplasm.get_sex_display() or "")

    def dehydrate_race(self, neoplasm):
        """Returns the race in str format."""
        return str(neoplasm.get_race_display() or "")

    def dehydrate_residence_municipality(self, neoplasm):
        """Returns the residence municipality in str format."""
        return str(neoplasm.residence_municipality or "")

    def dehydrate_born_municipality(self, neoplasm):
        """Returns the born municipality in str format."""
        return str(neoplasm.born_municipality or "")

    def dehydrate_is_oncologic(self, neoplasm):
        """Returns the is_oncologic in str format."""
        return str(
            "Sí"
            if neoplasm.is_oncologic is True
            else "No"
            if neoplasm.is_oncologic is False
            else ""
        )

    class Meta:
        """Meta class for PatientResource."""

        model = Patient
        fields = (
            "identity_card",
            "first_name",
            "last_name",
            "street",
            "number",
            "building",
            "apartment",
            "sex",
            "date_of_birth",
            "between_streets",
            "division",
            "medical_record",
            "residence_municipality",
            "born_municipality",
            "is_oncologic",
        )
