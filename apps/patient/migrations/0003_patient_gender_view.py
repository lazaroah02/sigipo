from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0002_auto_20220414_1725"),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                """
                CREATE OR REPLACE VIEW gender_count AS
                SELECT row_number() OVER () as id,
                    (
                        SELECT
                            Count(*)
                        FROM
                            patient_patient
                            WHERE
                                MOD(CAST(SUBSTRING(patient_patient.identity_card,10,1) AS INT), 2) <> 0
                    ) AS female_count,
                    (
                        SELECT
                            Count(*)
                        FROM
                            patient_patient
                        WHERE
                            MOD(CAST(SUBSTRING(patient_patient.identity_card,10,1) AS INT), 2) = 0
                    ) AS male_count ;
                """,
            ],
            reverse_sql=[
                "DROP VIEW gender_count;",
            ],
        )
    ]
