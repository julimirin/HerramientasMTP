# Generated by Django 2.0 on 2018-02-09 09:56

import GeneradorEvidencias.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeneradorEvidencias', '0024_auto_20180208_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='plan_de_pruebas',
            field=models.FileField(upload_to='GeneradorEvidencias/planes_de_prueba/', validators=[GeneradorEvidencias.validators.valid_extension]),
        ),
    ]