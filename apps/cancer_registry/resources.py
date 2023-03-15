from import_export.resources import Field, ModelResource

from apps.cancer_registry.models import Neoplasm


class NeoplasmResource(ModelResource):
    """
    Resource Subclass for handling how the
    resource model can be inported or exported
    """

    patient = Field(attribute="patient", column_name="Paciente")
    primary_site = Field(attribute="primary_site", column_name="Sitio primario")
    histologic_type = Field(attribute="histologic_type", column_name="Tipo histológico")
    laterality = Field(attribute="laterality", column_name="Lateralidad")
    date_of_diagnosis = Field(
        attribute="date_of_diagnosis", column_name="Fecha de diagnóstico"
    )
    age_at_diagnosis = Field(
        attribute="age_at_diagnosis", column_name="Edad de diagnóstico"
    )
    psa = Field(attribute="psa", column_name="PSA")

    diagnostic_confirmation = Field(
        attribute="diagnostic_confirmation", column_name="Confirmación del Diagnóstico"
    )
    differentiation_grade = Field(
        attribute="differentiation_grade", column_name="Grado de diferenciación"
    )
    clinical_extension = Field(
        attribute="clinical_extension", column_name="Extensión clínica"
    )
    clinical_stage = Field(attribute="clinical_stage", column_name="Estado clínico")
    is_pregnant = Field(attribute="is_pregnant", column_name="Embarazada")
    trimester = Field(attribute="trimester", column_name="Trimestre")
    is_vih = Field(attribute="is_vih", column_name="VIH")
    source_of_info = Field(
        attribute="source_of_info", column_name="Fuente de información"
    )
    date_of_report = Field(attribute="date_of_report", column_name="Fecha de reporte")
    medic_that_report = Field(
        attribute="medic_that_report", column_name="Médico que reportó"
    )
    tumor = Field(attribute="tumor", column_name="Tumor")
    nodule = Field(attribute="nodule", column_name="Nodulo")
    metastasis = Field(attribute="metastasis", column_name="Metástasis")
    neoplasm_classification = Field(
        attribute="neoplasm_classification", column_name="Clínico o Patológico"
    )
    tumor_classification = Field(
        attribute="tumor_classification", column_name="Clasificación"
    )
    treatment_performed = Field(
        attribute="treatment_performed", column_name="Tratamiento realizado"
    )
    group = Field(attribute="group", column_name="Grupo")
    hematological_transformation = Field(
        attribute="hematological_transformation",
        column_name="Transformación hematológica",
    )
    date_of_first_symptoms = Field(
        attribute="date_of_first_symptoms", column_name="Fecha de primeros síntomas"
    )
    acute_lymphoid_leukemia = Field(
        attribute="acute_lymphoid_leukemia", column_name="Leucemia linfoide aguda (FAB)"
    )
    chronic_lymphoid_leukemia = Field(
        attribute="chronic_lymphoid_leukemia", column_name="Leucemia crónica"
    )
    multiple_myeloma = Field(
        attribute="multiple_myeloma", column_name="Mieloma múltiple (Durie-Salmon)"
    )
    chronic_myeloid_leukemia = Field(
        attribute="chronic_myeloid_leukemia", column_name="Leucemia mieloide crónica"
    )
    acute_myeloid_leukemia = Field(
        attribute="acute_myeloid_leukemia", column_name="Leucemia mieloide aguda (FAB)"
    )

    def dehydrate_patient(self, neoplasm):
        """
        Returns the representation of the patient (name + last name + clinic history)
        column in the export

        Parameters:
        Neoplasm:neoplasm: a instance of Neoplasm model

        Returns:
        str:representation of the patient column to export
        """
        return str(neoplasm.patient)

    def dehydrate_laterality(self, neoplasm):
        """
        Returns the representation of the laterality column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the laterality column to export
        """
        return str(neoplasm.get_laterality_display() or "")

    def dehydrate_diagnostic_confirmation(self, neoplasm):
        """
        Returns the representation of the diagnostic confirmation column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the diagnostic confirmation column to export
        """
        return str(neoplasm.get_diagnostic_confirmation_display() or "")

    def dehydrate_differentiation_grade(self, neoplasm):
        """
        Returns the representation of the differentiation grade column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the differentiation grade column to export
        """
        return str(neoplasm.get_differentiation_grade_display() or "")

    def dehydrate_clinical_extension(self, neoplasm):
        """
        Returns the representation of the clinical extension column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the clinical extension column to export
        """
        return str(neoplasm.get_clinical_extension_display() or "")

    def dehydrate_clinical_stage(self, neoplasm):
        """
        Returns the representation of the clinical stage column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the clinical stage column to export
        """
        return str(neoplasm.get_clinical_stage_display() or "")

    def dehydrate_is_pregnant(self, neoplasm):
        """
        Returns the representation of the is pregnant column in the export
        ("Si" if the value is True, "No" if is False and "" otherwise)

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the is pregnant column to export ("Si", "No" or "")
        """
        return str(
            "Sí"
            if neoplasm.is_pregnant is True
            else "No"
            if neoplasm.is_pregnant is False
            else ""
        )

    def dehydrate_trimester(self, neoplasm):
        """
        Returns the representation of the trimester column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the trimester column to export
        """
        return str(neoplasm.trimester or "")

    def dehydrate_is_vih(self, neoplasm):
        """
        Returns the representation of the is vih column in the export
        ("Si" if the value is True, "No" if is False and "" otherwise)

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the is vih column to export ("Si", "No" or "")
        """
        return str(
            "Sí"
            if neoplasm.is_vih is True
            else "No"
            if neoplasm.is_vih is False
            else ""
        )

    def dehydrate_source_of_info(self, neoplasm):
        """
        Returns the representation of the source of info column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the source of info column to export
        """
        return str(neoplasm.get_source_of_info_display() or "")

    def dehydrate_medic_that_report(self, neoplasm):
        """
        Returns the representation of the medic that report column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the medic that report column to export
        """
        return str(neoplasm.medic_that_report or "")

    def dehydrate_tumor(self, neoplasm):
        """
        Returns the representation of the tumor column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the tumor column to export
        """
        return str(neoplasm.get_tumor_display() or "")

    def dehydrate_nodule(self, neoplasm):
        """
        Returns the representation of the nodule column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the nodule column to export
        """
        return str(neoplasm.get_nodule_display() or "")

    def dehydrate_metastasis(self, neoplasm):
        """
        Returns the representation of the metastasis column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the metastasis column to export
        """
        return str(neoplasm.get_metastasis_display() or "")

    def dehydrate_neoplasm_classification(self, neoplasm):
        """
        Returns the representation of the neoplasm classification column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the neoplasm classification column to export
        """
        return str(neoplasm.get_neoplasm_classification_display() or "")

    def dehydrate_tumor_classification(self, neoplasm):
        """
        Returns the representation of the tumor classification column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the tumor classification column to export
        """
        return str(neoplasm.get_tumor_classification_display() or "")

    def dehydrate_treatment_performed(self, neoplasm):
        """
        Returns the representation of the treatment performed column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the treatment performed column to export
        """
        return str(neoplasm.get_treatment_performed_display() or "")

    def dehydrate_group(self, neoplasm):
        """
        Returns the representation of the group column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the group column to export
        """
        return str(neoplasm.group or "")

    def dehydrate_hematological_transformation(self, neoplasm):
        """
        Returns the representation of the hematological transformation column in the export
        ("Si" if the value is True, "No" if is False and "" otherwise)

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the hematological transformation column to export ("Si", "No" or "")
        """
        return str(
            "Sí"
            if neoplasm.hematological_transformation is True
            else "No"
            if neoplasm.hematological_transformation is False
            else ""
        )

    def dehydrate_acute_lymphoid_leukemia(self, neoplasm):
        """
        Returns the representation of the acute lymphoid leukemia column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the acute lymphoid leukemia column to export
        """
        return str(neoplasm.get_acute_lymphoid_leukemia_display() or "")

    def dehydrate_chronic_lymphoid_leukemia(self, neoplasm):
        """
        Returns the representation of the chronic lymphoid leukemia column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the chronic lymphoid leukemia column to export
        """
        return str(neoplasm.get_chronic_lymphoid_leukemia_display() or "")

    def dehydrate_multiple_myeloma(self, neoplasm):
        """
        Returns the representation of the multiple myeloma column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the multiple myeloma column to export
        """
        return str(neoplasm.get_multiple_myeloma_display() or "")

    def dehydrate_chronic_myeloid_leukemia(self, neoplasm):
        """
        Returns the representation of the chronic myeloid leukemia column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the chronic myeloid leukemia column to export
        """
        return str(neoplasm.get_chronic_myeloid_leukemia_display() or "")

    def dehydrate_acute_myeloid_leukemia(self, neoplasm):
        """
        Returns the representation of the acute myeloid leukemia column in the export

        Parameters:
        neoplasm (Neoplasm): a instance of Neoplasm model

        Returns:
        str:representation of the acute myeloid leukemia column to export
        """
        return str(neoplasm.get_acute_myeloid_leukemia_display() or "")

    class Meta:
        """
        It handles the model fields that will be representated in the export columns
        """

        model = Neoplasm
        fields = (
            "patient",
            "date_of_diagnosis",
            "age_at_diagnosis",
            "psa",
            "primary_site",
            "laterality",
            "diagnostic_confirmation",
            "histologic_type",
            "differentiation_grade",
            "clinical_extension",
            "clinical_stage",
            "is_pregnant",
            "trimester",
            "is_vih",
            "source_of_info",
            "date_of_report",
            "medic_that_report",
            "tumor",
            "nodule",
            "metastasis",
            "neoplasm_classification",
            "tumor_classification",
            "treatment_performed",
            "group",
            "hematological_transformation",
            "date_of_first_symptoms",
            "acute_lymphoid_leukemia",
            "chronic_lymphoid_leukemia",
            "acute_myeloid_leukemia",
            "multiple_myeloma",
            "chronic_myeloid_leukemia",
        )
