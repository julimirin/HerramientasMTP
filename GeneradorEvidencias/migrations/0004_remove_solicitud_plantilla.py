# Generated by Django 2.0 on 2018-02-16 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeneradorEvidencias', '0003_auto_20180216_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='plantilla',
        ),
    ]
