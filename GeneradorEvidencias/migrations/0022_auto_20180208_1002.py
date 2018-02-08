# Generated by Django 2.0 on 2018-02-08 09:02

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('GeneradorEvidencias', '0021_auto_20180208_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fase_de_prueba',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cliente', chained_model_field='fase_de_prueba', on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.FasePrueba'),
        ),
    ]
