from django.db.models import (
    CASCADE,
    AutoField,
    FloatField,
    ForeignKey,
    ManyToManyField,
    OneToOneField,
    TextChoices,
    TextField,
    DateTimeField,
    DateField,
    TimeField,
    CharField,
    IntegerField,
)
from django.db.models.manager import Manager
from multiselectfield import MultiSelectField

from apps.core.models import TimeStampedModel
from apps.patient.models import Patient



class OtherClinicalDiagnosesChoices(TextChoices):
    """Other Clinical Diagnoses"""

    IMA = "Infarto del Miocardio agudo", "Infarto del Miocardio agudo"
    IMANT = "Infarto del Miocardio antiguo", "Infarto del Miocardio antiguo"
    HART = "Hipertensión Arterial", "Hipertensión Arterial"

    ECV = "Enfermedades cardiovasculares", "Enfermedades cardiovasculares"
    ECVH = "E.C.V Hemorrágica", "E.C.V Hemorrágica"
    ECVO = "E.C.V Oclusiva", "E.C.V Oclusiva"
    
    TMAL = "Tumor Maligno", "Tumor Maligno"
    TRPL = "Tromboembolia Pulmonar", "Tromboembolia Pulmonar"
    DBML = "Diabetes Mellitus","Diabetes Mellitus"
    CRHP = "Cirrosis Hepática", "Cirrosis Hepática"
    FAILMO = "Fallo Multiorgánico","Fallo Multiorgánico"

    INFCT = "Infección","Infección"
    BRNEUM = "Bronconeumonía","Bronconeumonía"
    TBC = "Tuberculosis", "Tuberculosis"
    OTHER = "Otras","Otras"

    DTHM = "Muerte Materna", "Muerte Materna"
    DR = "Directa", "Directa"
    IDR = "Indirecta", "Indirecta"
    ACDNT = "Accidental (No Obstetrica)", "Accidental (No Obstetrica)"
    LATE = "Tardía","Tardía"

    VILDTH = "Muerte por hecho violento", "Muerte por hecho violento"
    SUICD = "Suicidio", "Suicidio"
    HMCD  = "Homicidio", "Homicidio"
    TRACC = "Accidente de Transito","Accidente de Transito"
    OTACC = "Otros Accidentes","Otros Accidentes"
    TAB = "Tabaquismo", "Tabaquismo"
    ALCH = "Alcoholismo","Alcoholismo"
    TRPLA = "Transplante","Transplante"
    IRCR = "Insufuciencia Renal Cronica","Insufuciencia Renal Cronica"
    OBSI = "Obesidad", "Obesidad"

class PathologyQuerysetManager(Manager):
    """Manager to handle patient."""

    def get_queryset(self):
        """Fetch the related patient."""
        return super().get_queryset().select_related("patient")

class Pathology(TimeStampedModel):
    """Model representation of External Beam Treatment."""

    patient = ForeignKey(Patient, null=False, blank=False, on_delete=CASCADE)
    authopsy_number = AutoField(verbose_name ='Número de Autopsia',primary_key=True, unique=True)
    entry_date = DateField(verbose_name ='Fecha de ingreso',null=True, blank=True)
    exit_date = DateField(verbose_name ='Fecha de egreso',null=True, blank=True)
    eval_speciality = TextField(verbose_name ='Egreso (Especialidad)',null=True, blank=True)
    eviseration_date = DateField(verbose_name ='Fecha de eviseración',null=True, blank=True)
    eviseration_by = TextField(verbose_name ='Por (Eviseración)',null=True, blank=True)
    disection_date = DateField(verbose_name ='Fecha de disección',null=True, blank=True)
    disection_by = TextField(verbose_name ='Por (Disección)',null=True, blank=True)
    dignostic_date = DateField(verbose_name ='Fecha de diagnóstico',null=True, blank=True)
    diagnostic_by = TextField(verbose_name ='Por (Diagnóstico)',null=True, blank=True)
    study_full = TextField(verbose_name ='Estudio Completo',null=True, blank=True)
    study_micro = TextField(verbose_name ='Estudio Micro',null=True, blank=True)
    hc_resume = TextField(verbose_name ='Resumen de Historia Clínica',null=True, blank=True)

    #####################################Clinical Diagnoses######################################################

    CDM = TextField(verbose_name ='Diagnóstico Clínico CDM',null=True, blank=True)
    CIM = TextField(verbose_name ='Diagnóstico Clínico CIM',null=True, blank=True)
    CIM = TextField(verbose_name ='Diagnóstico Clínico CIM',null=True, blank=True)
    CBM = TextField(verbose_name ='Diagnóstico Clínico CBM',null=True, blank=True)
    CC = TextField(verbose_name ='Diagnóstico Clínico CC',null=True, blank=True)
    CC = TextField(verbose_name ='Diagnóstico Clínico CC',null=True, blank=True)

    tests = MultiSelectField(
        choices=OtherClinicalDiagnosesChoices.choices,
        min_choices=1,
        max_choices=14,
        max_length=250,
    )

###################################################################################################################

    external_habit = TextField(verbose_name ='Hábito externo',null=True, blank=True)
    internal_habit = TextField(verbose_name ='Hábito interno',null=True, blank=True)
    cavities = TextField(verbose_name ='Cavidades',null=True, blank=True)
    nerv_sistem = TextField(verbose_name ='Sistema Nervioso',null=True, blank=True)
    respiratory_aparatus = TextField(verbose_name ='Aparato Respiratorio',null=True, blank=True)
    cardiovascular_aparatus = TextField(verbose_name ='Aparato Cardiovascular',null=True, blank=True)
    digestive_aparatus = TextField(verbose_name ='Aparato Disgestivo',null=True, blank=True)
    urinal_aparatus = TextField(verbose_name ='Aparato Urinario',null=True, blank=True)
    genital_aparatus = TextField(verbose_name ='Aparato Genital',null=True, blank=True)
    hemollymphoietic_aparatus = TextField(verbose_name ='Aparato Hemolinfopoyético',null=True, blank=True)
    endocrine_system = TextField(verbose_name ='Sistema Endocrino',null=True, blank=True)
    osteo_mio_articular_system = TextField(verbose_name ='Sistema Osteo-Mio-Articular',null=True, blank=True)

    ######################Messurements#############################################################
    
    brain_weight = FloatField(verbose_name ='Peso del Cerebro',null=True, blank=True)
    cerebellum_stream_w = FloatField(verbose_name ='Peso Cerebelo y Tallo',null=True, blank=True)
    right_lung_w = FloatField(verbose_name ='Peso del Pulmón derecho',null=True, blank=True)
    left_lung_w = FloatField(verbose_name ='Peso del Pulmón izquierdo',null=True, blank=True)
    heart_w = FloatField(verbose_name ='Peso del Corazón',null=True, blank=True)
    VI = FloatField(verbose_name ='VI (mm)',null=True, blank=True)
    VD = FloatField(verbose_name ='VD (mm)',null=True, blank=True)
    t_valve = FloatField(verbose_name ='Válvula T (mm)',null=True, blank=True)
    p_valve = FloatField(verbose_name ='Válvula P (mm)',null=True, blank=True)
    M = FloatField(verbose_name ='M (mm)',null=True, blank=True)
    A = FloatField(verbose_name ='A (mm)',null=True, blank=True)
    liver_w = FloatField(verbose_name ='Peso del Hígado',null=True, blank=True)
    r_kidney_w = FloatField(verbose_name ='Peso del Riñón derecho',null=True, blank=True)
    r_kidney_v = FloatField(verbose_name ='Volumen del Riñón derecho',null=True, blank=True)
    l_kidney_w = FloatField(verbose_name ='Peso del Riñón izquierdo',null=True, blank=True)
    l_kidney_v = FloatField(verbose_name ='Volumen del Riñón izquierdo',null=True, blank=True)
    pancreas_w = FloatField(verbose_name ='Peso del Páncreas',null=True, blank=True)
    spleen_w = FloatField(verbose_name ='Peso del Bazo',null=True, blank=True)
    thyroid = FloatField(verbose_name ='Peso del Tiroides',null=True, blank=True)

    ###############################################################################################
    macroscopic_conclusions = TextField(verbose_name ='Conclusiones Macroscópicas',null=True, blank=True)
    
    ###############Final Anatopathologic Dignose######################################
    CDM = TextField(verbose_name ='Diagnóstico Clínico CDM',null=True, blank=True)
    CIM = TextField(verbose_name ='Diagnóstico Clínico CIM',null=True, blank=True)
    CIM = TextField(verbose_name ='Diagnóstico Clínico CIM',null=True, blank=True)
    CBM = TextField(verbose_name ='Diagnóstico Clínico CBM',null=True, blank=True)
    CC = TextField(verbose_name ='Diagnóstico Clínico CC',null=True, blank=True)
    CC = TextField(verbose_name ='Diagnóstico Clínico CC',null=True, blank=True)

    other_anatopathologic_dignose = TextField(verbose_name ='Otros Diagnósticos Anatopatológicos',null=True, blank=True)

    ########################################################################
    observation_epicrisis = TextField(verbose_name ='Observaciones (Epicrisis)',null=True, blank=True)

    pathologist = TextField(verbose_name ='Patólogo',null=True, blank=True)


    objects = PathologyQuerysetManager()

    class Meta:
        verbose_name = "Infrome de Autopsia"
        verbose_name_plural = "Informes de Autopsia"
        ordering = ["created_at"]
        default_permissions = ()

    def __str__(self):
        """Returns the str representation for the model."""
        return f"Muestra {str(self.sample_number).zfill(2)} {str(self.tests)}"