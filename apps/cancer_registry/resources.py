from import_export.resources import Field, ModelResource

from apps.cancer_registry.models import Neoplasm


class NeoplasmResource(ModelResource):
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
        return str(neoplasm.patient)

    def dehydrate_laterality(self, neoplasm):
        return str(neoplasm.get_laterality_display() or "")

    def dehydrate_diagnostic_confirmation(self, neoplasm):
        return str(neoplasm.get_diagnostic_confirmation_display() or "")

    def dehydrate_differentiation_grade(self, neoplasm):
        return str(neoplasm.get_differentiation_grade_display() or "")

    def dehydrate_clinical_extension(self, neoplasm):
        return str(neoplasm.get_clinical_extension_display() or "")

    def dehydrate_clinical_stage(self, neoplasm):
        return str(neoplasm.get_clinical_stage_display() or "")

    def dehydrate_is_pregnant(self, neoplasm):
        return str(
            "Sí"
            if neoplasm.is_pregnant is True
            else "No"
            if neoplasm.is_pregnant is False
            else ""
        )

    def dehydrate_trimester(self, neoplasm):
        return str(neoplasm.trimester or "")

    def dehydrate_is_vih(self, neoplasm):
        return str(
            "Sí"
            if neoplasm.is_vih is True
            else "No"
            if neoplasm.is_vih is False
            else ""
        )

    def dehydrate_source_of_info(self, neoplasm):
        return str(neoplasm.get_source_of_info_display() or "")

    def dehydrate_medic_that_report(self, neoplasm):
        return str(neoplasm.medic_that_report or "")

    def dehydrate_tumor(self, neoplasm):
        return str(neoplasm.get_tumor_display() or "")

    def dehydrate_nodule(self, neoplasm):
        return str(neoplasm.get_nodule_display() or "")

    def dehydrate_metastasis(self, neoplasm):
        return str(neoplasm.get_metastasis_display() or "")

    def dehydrate_neoplasm_classification(self, neoplasm):
        return str(neoplasm.get_neoplasm_classification_display() or "")

    def dehydrate_tumor_classification(self, neoplasm):
        return str(neoplasm.get_tumor_classification_display() or "")

    def dehydrate_treatment_performed(self, neoplasm):
        return str(neoplasm.get_treatment_performed_display() or "")

    def dehydrate_group(self, neoplasm):
        return str(neoplasm.group or "")

    def dehydrate_hematological_transformation(self, neoplasm):
        return str(
            "Sí"
            if neoplasm.hematological_transformation is True
            else "No"
            if neoplasm.hematological_transformation is False
            else ""
        )

    def dehydrate_acute_lymphoid_leukemia(self, neoplasm):
        return str(neoplasm.get_acute_lymphoid_leukemia_display() or "")

    def dehydrate_chronic_lymphoid_leukemia(self, neoplasm):
        return str(neoplasm.get_chronic_lymphoid_leukemia_display() or "")

    def dehydrate_multiple_myeloma(self, neoplasm):
        return str(neoplasm.get_multiple_myeloma_display() or "")

    def dehydrate_chronic_myeloid_leukemia(self, neoplasm):
        return str(neoplasm.get_chronic_myeloid_leukemia_display() or "")

    def dehydrate_acute_myeloid_leukemia(self, neoplasm):
        return str(neoplasm.get_acute_myeloid_leukemia_display() or "")

    class Meta:
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
