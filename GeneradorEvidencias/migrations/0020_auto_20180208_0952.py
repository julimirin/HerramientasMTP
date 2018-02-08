# Generated by Django 2.0 on 2018-02-08 08:52

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('GeneradorEvidencias', '0019_auto_20180207_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cliente',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='entorno',
            name='entorno',
            field=models.CharField(max_length=50),
        ),
        migrations.RemoveField(
            model_name='faseprueba',
            name='cliente',
        ),
        migrations.AddField(
            model_name='faseprueba',
            name='cliente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.Cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='entorno',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cliente', chained_model_field='cliente', on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.Entorno'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='nombre_proyecto',
            field=models.CharField(max_length=100),
        ),
    ]
