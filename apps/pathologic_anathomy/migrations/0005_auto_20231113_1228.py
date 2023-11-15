# Generated by Django 3.2.16 on 2023-11-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pathologic_anathomy", "0004_head"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="head",
            name="a",
        ),
        migrations.AddField(
            model_name="head",
            name="aditional_tumor_size",
            field=models.FloatField(
                default=0,
                verbose_name="Las dimensiones adicionales del tumor (centímetros):",
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="carcinoma_papilar",
            field=models.IntegerField(
                choices=[
                    (1, "Carcinoma Papilar, Clásico (usual, convencional)"),
                    (
                        2,
                        "Carcinoma Papilar, variante folicular, encapsulado / bien delimitado, con invasión tumoral a la capsula",
                    ),
                    (
                        3,
                        "Carcinoma Papilar, variante folicular, encapsulado / bien delimitado, no-invasivo",
                    ),
                    (4, "Carcinoma Papilar, variante folicular, infiltrativo"),
                    (5, "Carcinoma Papilar, variante de células alta"),
                    (6, "Carcinoma Papilar, variante morular cribiforme"),
                    (7, "Carcinoma Papilar, variante de esclerosis difusa"),
                    (8, "Carcinoma Papilar, otra variante (especifique)"),
                    (9, "Carcinoma Papilar"),
                    (
                        10,
                        "Neoplasia tiroidea folicular na invasiva con caracteres nucleares similares al papilar",
                    ),
                ],
                default=None,
                verbose_name="Carcinoma Papilar:",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="carcinomas_foliculares",
            field=models.IntegerField(
                choices=[
                    (1, "Carcinoma folicular, minimamente invasivo"),
                    (2, "Carcinoma folicular, angioinvasivo encapsulado"),
                    (3, "Carcinoma folicular, ampliamente invasivo"),
                    (
                        4,
                        "Carcinoma folicular, minimamente invasivo, oncocítico (células de Hürthle)",
                    ),
                    (
                        5,
                        "Carcinoma folicular, angioinvasivo encapsulado, oncocítico (células de Hürthle)",
                    ),
                    (
                        6,
                        "Carcinoma folicular, ampliamente invasivo, oncocítico (células de Hürthle)",
                    ),
                    (
                        7,
                        "Carcinoma folicular, minimamente invasivo, otra variante (especifique)",
                    ),
                    (
                        8,
                        "Carcinoma folicular, angioinvasivo encapsulado, otra variante (especifique)",
                    ),
                    (
                        9,
                        "Carcinoma folicular, ampliamente invasivo, otra variante (especifique)",
                    ),
                    (10, "Carcinoma folicular"),
                    (11, "Carcinoma tiroideo pobremente diferenciado"),
                    (
                        12,
                        "Carcinoma indiferenciado (anaplásico), con un componente focal o menor, sin extensión extra tiroidea",
                    ),
                    (
                        13,
                        "Carcinoma indiferenciado (anaplásico), con un componente mayor",
                    ),
                    (
                        14,
                        "Carcinoma indiferenciado (anaplásico), no especificado en otra forma",
                    ),
                    (15, "Carcinoma medular"),
                    (16, "Carcinoma, el tipo no puede ser determinado"),
                    (
                        17,
                        "Otro tipo del histológico que no figura en la lista (especifique)",
                    ),
                ],
                default=None,
                verbose_name="Carcinomas Foliculares",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="distancia_carcinoma_mas_cercano",
            field=models.FloatField(
                blank=True,
                null=True,
                verbose_name="La distancia del carcinoma invasivo de los  márgenes más cercano (milímetros):",
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="extension",
            field=models.CharField(
                blank=True,
                choices=[
                    (1, "Invade solamente las bandas musculares (ie, pT3b)"),
                    (
                        2,
                        "Invade tejidos celular subcutáneo, laringe, tráquea, esófago o nervio laríngeo recurrente (ie, PT4a)",
                    ),
                    (
                        3,
                        "Invadiendo la fascia pre-vertebral o recubriendo la arteria carótida o los vasos mediastinales (ie,pT4b)",
                    ),
                ],
                max_length=10,
                null=True,
                verbose_name="La extensión (requiere clínica /invasión macroscópica y microscópica del tumor):",
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="extension_extratiroidea",
            field=models.IntegerField(
                choices=[
                    (1, "No identificado"),
                    (2, "Presente"),
                    (3, "No puede ser determinado"),
                ],
                default=None,
                verbose_name="Extensión Extra-tiroidea:",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="focalidad_tumor",
            field=models.IntegerField(
                choices=[
                    (1, "Unifocal"),
                    (2, "Multifocal"),
                    (3, "No puede ser determinado"),
                ],
                default=None,
                verbose_name="Focalidad del Tumor:",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="ganglio_linfatico_encontrado",
            field=models.BooleanField(
                default=False, verbose_name="Ganglio linfático presente o encontrado"
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="indice_mitosis",
            field=models.FloatField(
                default=0,
                verbose_name="Índice de mitosis por 2 mm2:\n        Nota: La Mitosis debería ser contada en 10 campos de alto poder consecutivos (HPF) a 400x en el área más activa de mitosis. \n        Para la mayoría de los microscopios, 10 (HPF) es aproximadamente equivalente a 2.5 mm2",
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="invasion_linfatica",
            field=models.IntegerField(
                choices=[
                    (1, "No identificado"),
                    (2, "Presente"),
                    (3, "No puede ser determinado"),
                ],
                default=None,
                verbose_name="Invasión Linfática (Nota J)",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="invasion_perineural",
            field=models.IntegerField(
                choices=[
                    (1, "No identificado"),
                    (2, "Presente"),
                    (3, "No puede ser determinado"),
                ],
                default=None,
                verbose_name="Invasión peri-neural",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="invasion_vascular",
            field=models.IntegerField(
                choices=[
                    (1, "No identificado"),
                    (2, "Presente"),
                    (3, "No puede ser determinado"),
                    (4, "Focal (menos de 4 vasos)"),
                    (5, "Extensa (4 o más vasos)"),
                ],
                default=None,
                verbose_name="Invasion Vacular",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="localizacion_tumor",
            field=models.CharField(
                choices=[
                    ("lobulo_derecho", "El lóbulo derecho"),
                    ("lobulo_izquierdo", "El lóbulo izquierdo"),
                    ("istmo", "El istmo"),
                    ("lobulo_piramidal", "El lóbulo piramidal"),
                    ("otro", "Otro (especifique)"),
                ],
                default=None,
                max_length=100,
                verbose_name="El sitio (o localización) del tumor (seleccione todo lo que aplique):",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="localizacion_tumor_otro",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="head",
            name="margenes",
            field=models.IntegerField(
                choices=[
                    (1, "No puede ser evaluado"),
                    (2, "No invadido por el carcinoma"),
                    (3, "Invadido por el carcinoma"),
                ],
                default=None,
                verbose_name="Los Margenes",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="max_tumor_size",
            field=models.FloatField(
                default=None,
                verbose_name="La máxima dimensión del tumor en centímetros:",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="niveles_ganglionares",
            field=models.CharField(
                choices=[
                    (
                        "nivel_Vi",
                        "Nivel VI: pre- traqueal, para- traqueal y pre-laríngeo/Delphian, peri-tiroideos (disección del compartimiento central)",
                    ),
                    (
                        "nivel_VII",
                        "Nivel VII (los ganglios linfáticos mediastinales superiores)",
                    ),
                    (
                        "nivel_IV_derecho",
                        "Nivel I-V (disección lateral del cuello) Derecho",
                    ),
                    (
                        "nivel_IV_izquierdo",
                        "Nivel I-V (disección lateral del cuello) Izquierda",
                    ),
                ],
                default=None,
                max_length=100,
                verbose_name="Especifique Niveles Ganglionares (seleccione todo lo que aplique)",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="num_ganglios_linfaticos",
            field=models.IntegerField(
                default=None,
                verbose_name="El examen del ganglio linfático (es únicamente requerido si hay ganglios linfáticos presentes en el espécimen)",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="num_ganglios_linfaticos_examinados",
            field=models.IntegerField(
                default=0, verbose_name="El Número de Ganglios Linfáticos Examinados: "
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="num_ganglios_linfaticos_examinados_no_determinado",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name="head",
            name="num_ganglios_no_determinados",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                verbose_name="El número de ganglios no puede ser determinado (explique):",
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="otro_tipo_carcinoma_folicular",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                verbose_name="Otro tipo del histológico que no figura en la lista (especifique): ",
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="sitios_invasion",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                verbose_name="Sitio(s) de Invasión:",
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="tipo_extension_parcial",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="head",
            name="tipo_muestra",
            field=models.IntegerField(
                choices=[
                    (1, "Completamiento de tiroidectomía"),
                    (2, "Excisión parcial derecha"),
                    (3, "Excisión parcial izquierda"),
                    (4, "Excisión parcial (especifique tipo, si es posible)"),
                    (5, "Lobectomía derecha"),
                    (6, "Lobectomía izquierda"),
                    (7, "Lobectomía derecha con istmectomía (hemitiroidectomía)"),
                    (8, "Lobectomía izquierda con istmectomía (hemitiroidectomía)"),
                    (
                        9,
                        "Lóbulo derecho con lobectomía parcial izquierda (tiroidectomía subtotal o casi total)",
                    ),
                    (
                        10,
                        "Lóbulo izquierdo con lobectomía parcial derecha (tiroidectomía subtotal o casi total)",
                    ),
                    (11, "Tiroidectomía total"),
                ],
                default=None,
                verbose_name="Tipo de muestra:",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="head",
            name="tumor_size_imposible_to_determinate",
            field=models.CharField(
                blank=True,
                max_length=1000,
                null=True,
                verbose_name="Dimensiones imposibles de determinar. Explique porque:",
            ),
        ),
        migrations.AddField(
            model_name="head",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]