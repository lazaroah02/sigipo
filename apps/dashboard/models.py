from django.db.models import IntegerField, Model


class GenderCountView(Model):
    """View to get the count of patients by sex and total."""

    female_count = IntegerField()
    male_count = IntegerField()
    total_count = IntegerField()

    class Meta:
        managed = False
        db_table = "GENDER_COUNT"
