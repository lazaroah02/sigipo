from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("patient", "0008_patient_patient_pat_last_na_90bcb7_idx_and_more"),
    ]
    operations = [
        migrations.RunSQL(
            sql=[
                """
                CREATE OR REPLACE VIEW GENDER_COUNT AS 
                    SELECT
                        row_number() OVER () as id, (
                            SELECT
                                CAST(Count(*) AS INTEGER)
                            FROM
                                patient_patient
                            WHERE
                                patient_patient.sex = 2
                                AND patient_patient.is_oncologic
                        ) AS female_count, (
                            SELECT
                                CAST(Count(*) AS INTEGER)
                            FROM
                                patient_patient
                            WHERE
                                patient_patient.sex = 1
                                AND patient_patient.is_oncologic
                        ) AS male_count, (
                            SELECT
                                CAST(Count(*) AS INTEGER)
                            FROM
                                patient_patient
                            WHERE
                                patient_patient.is_oncologic
                        ) AS
                TOTAL_COUNT; 
                """
                if not settings.MY_SQL_DB
                else """
                CREATE OR REPLACE VIEW GENDER_COUNT AS 
                    SELECT
                        row_number() OVER () as id, (
                            SELECT
                                CAST(Count(*) AS SIGNED)
                            FROM
                                patient_patient
                            WHERE
                                patient_patient.sex = 2
                                AND patient_patient.is_oncologic
                        ) AS female_count, (
                            SELECT
                                CAST(Count(*) AS SIGNED)
                            FROM
                                patient_patient
                            WHERE
                                patient_patient.sex = 1
                                AND patient_patient.is_oncologic
                        ) AS male_count, (
                            SELECT
                                CAST(Count(*) AS SIGNED)
                            FROM
                                patient_patient
                            WHERE
                                patient_patient.is_oncologic
                        ) AS
                TOTAL_COUNT; 
                """,
            ],
            reverse_sql=[
                "DROP VIEW GENDER_COUNT;",
            ],
        )
    ]
