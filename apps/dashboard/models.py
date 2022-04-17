from django.db.models import IntegerField, Model


class GenderCountView(Model):
    female_count = IntegerField()
    male_count = IntegerField()

    class Meta:
        managed = False
        db_table = "gender_count"
