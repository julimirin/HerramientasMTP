# Generated by Django 2.0 on 2018-02-21 10:45

import GeneradorEvidencias.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CasoPrueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_caso', models.CharField(max_length=6)),
                ('nombre_caso', models.CharField(max_length=50)),
                ('descripcion_caso', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Entorno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entorno', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='FasePrueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fase_de_prueba', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PasoPrueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_paso', models.CharField(max_length=10)),
                ('descripcion_paso', models.CharField(max_length=500)),
                ('resultado_paso', models.CharField(max_length=500)),
                ('codigo_caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.CasoPrueba')),
            ],
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantilla', models.FileField(upload_to='GeneradorEvidencias/plantillas/')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_proyecto', models.CharField(max_length=50)),
                ('nombre_proyecto', models.CharField(max_length=50)),
                ('archivo', models.FileField(upload_to='planes_de_prueba', validators=[GeneradorEvidencias.validators.validate_file_extension])),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.Cliente')),
                ('entorno', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cliente', chained_model_field='cliente', on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.Entorno')),
                ('fase_de_prueba', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cliente', chained_model_field='cliente', on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.FasePrueba')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='pasoprueba',
            unique_together={('codigo_caso', 'numero_paso')},
        ),
        migrations.AlterUniqueTogether(
            name='faseprueba',
            unique_together={('cliente', 'fase_de_prueba')},
        ),
        migrations.AlterUniqueTogether(
            name='entorno',
            unique_together={('cliente', 'entorno')},
        ),
    ]
