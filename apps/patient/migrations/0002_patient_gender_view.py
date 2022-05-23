from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                """
                CREATE OR REPLACE VIEW gender_count AS
                SELECT row_number() OVER () as id,
                    (
                        SELECT
                            CAST(Count(*) AS INTEGER)
                        FROM
                            patient_patient
                            WHERE
                                MOD(CAST(SUBSTRING(patient_patient.identity_card,10,1) AS INT), 2) <> 0 AND patient_patient.is_oncologic
                    ) AS female_count,
                    (
                        SELECT
                            CAST(Count(*) AS INTEGER)
                        FROM
                            patient_patient
                        WHERE
                            MOD(CAST(SUBSTRING(patient_patient.identity_card,10,1) AS INT), 2) = 0 AND patient_patient.is_oncologic
                    ) AS male_count;
                """,
            ],
            reverse_sql=[
                "DROP VIEW gender_count;",
            ],
        )
    ]
