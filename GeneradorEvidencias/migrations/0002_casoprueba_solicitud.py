# Generated by Django 2.0 on 2018-02-21 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GeneradorEvidencias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casoprueba',
            name='solicitud',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='GeneradorEvidencias.Solicitud'),
            preserve_default=False,
        ),
    ]
